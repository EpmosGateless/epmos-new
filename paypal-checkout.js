(() => {
  const state = { catalog: [], selected: null };
  const $ = (id) => document.getElementById(id);
  const money = (value) => new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" }).format(Number(value));

  function setStatus(message, kind = "info") {
    const el = $("checkout-status");
    if (!el) return;
    el.textContent = message;
    el.dataset.kind = kind;
  }

  function renderCatalog(catalog) {
    const select = $("service-sku");
    if (!select) return;
    select.innerHTML = "";
    const grouped = new Map();
    catalog.forEach((item) => {
      if (!grouped.has(item.category)) grouped.set(item.category, []);
      grouped.get(item.category).push(item);
    });
    [...grouped.keys()].sort().forEach((category) => {
      const group = document.createElement("optgroup");
      group.label = category;
      grouped.get(category).sort((a, b) => a.name.localeCompare(b.name)).forEach((item) => {
        const option = document.createElement("option");
        option.value = item.sku;
        option.textContent = `${item.name} — ${money(item.amount)}`;
        group.appendChild(option);
      });
      select.appendChild(group);
    });
    state.selected = catalog[0] || null;
    updateSelection();
  }

  function updateSelection() {
    const sku = $("service-sku")?.value;
    state.selected = state.catalog.find((item) => item.sku === sku) || state.catalog[0] || null;
    if (!state.selected) return;
    $("selected-service").textContent = state.selected.name;
    $("selected-price").textContent = money(state.selected.amount);
    $("selected-sku").textContent = state.selected.sku;
  }

  function loadPayPal(clientId) {
    return new Promise((resolve, reject) => {
      if (window.paypal) return resolve();
      const script = document.createElement("script");
      script.src = `https://www.paypal.com/sdk/js?client-id=${encodeURIComponent(clientId)}&currency=USD&components=buttons&enable-funding=venmo,paylater,card`;
      script.async = true;
      script.onload = resolve;
      script.onerror = () => reject(new Error("PayPal checkout could not be loaded."));
      document.head.appendChild(script);
    });
  }

  function renderButtons() {
    if (!window.paypal || !$("paypal-button-container")) return;
    window.paypal.Buttons({
      style: { layout: "vertical", shape: "rect", label: "paypal" },
      createOrder: async () => {
        updateSelection();
        if (!state.selected) throw new Error("Choose an EPMOS service first.");
        setStatus("Creating secure PayPal order…");
        const response = await fetch("/api/paypal/create-order", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ sku: state.selected.sku })
        });
        const data = await response.json();
        if (!response.ok || !data.orderId) throw new Error(data.error || "Unable to create order.");
        return data.orderId;
      },
      onApprove: async (data) => {
        setStatus("Confirming payment…");
        const response = await fetch("/api/paypal/capture-order", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ orderId: data.orderID, sku: state.selected.sku })
        });
        const result = await response.json();
        if (!response.ok || result.status !== "COMPLETED") throw new Error(result.error || "Payment could not be confirmed.");
        $("checkout-panel").hidden = true;
        $("payment-success").hidden = false;
        $("success-service").textContent = result.service;
        $("success-amount").textContent = money(result.amount.value);
        $("success-order").textContent = result.orderId;
        setStatus("Payment completed.", "success");
      },
      onCancel: () => setStatus("Payment was cancelled. No charge was completed.", "warning"),
      onError: (error) => {
        console.error("paypal_checkout_error", error);
        setStatus(error?.message || "Checkout could not be completed. Please try again.", "error");
      }
    }).render("#paypal-button-container");
  }

  async function init() {
    try {
      setStatus("Loading secure checkout…");
      const response = await fetch("/api/paypal/config", { cache: "no-store" });
      const config = await response.json();
      if (!response.ok || !config.clientId || !Array.isArray(config.catalog)) throw new Error(config.error || "Checkout is unavailable.");
      state.catalog = config.catalog;
      renderCatalog(state.catalog);
      $("service-sku")?.addEventListener("change", updateSelection);
      await loadPayPal(config.clientId);
      renderButtons();
      setStatus("Secure checkout ready.", "success");
    } catch (error) {
      console.error("paypal_checkout_init_failed", error);
      setStatus(error.message || "Secure checkout is temporarily unavailable.", "error");
    }
  }

  document.addEventListener("DOMContentLoaded", init);
})();
