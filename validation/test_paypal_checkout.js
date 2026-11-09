const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { CATALOG, getCatalogItem, publicCatalog } = require("../api/paypal/catalog");

const entries = Object.entries(CATALOG);
assert.equal(entries.length, 40, "catalog must contain the governed 40 fixed-price offerings");

for (const [sku, item] of entries) {
  assert.match(sku, /^EPM-[A-Z0-9-]+$/, `invalid SKU: ${sku}`);
  assert.equal(typeof item.name, "string");
  assert.equal(typeof item.category, "string");
  assert.match(item.amount, /^\d+\.\d{2}$/);
  assert.ok(Number(item.amount) > 0, `${sku} must have a positive price`);
  assert.deepEqual(getCatalogItem(sku), item);
}

assert.equal(getCatalogItem("UNKNOWN-SKU"), null);
const pub = publicCatalog();
assert.equal(pub.length, entries.length);
assert.ok(pub.every((item) => item.currency === "USD"));

const checkoutJs = fs.readFileSync(path.join(__dirname, "..", "paypal-checkout.js"), "utf8");
assert.ok(checkoutJs.includes('/api/paypal/create-order'));
assert.ok(checkoutJs.includes('/api/paypal/capture-order'));
assert.ok(checkoutJs.includes('JSON.stringify({ sku: state.selected.sku })'));
assert.ok(!checkoutJs.includes('PAYPAL_CLIENT_SECRET'));

const paymentHtml = fs.readFileSync(path.join(__dirname, "..", "pages", "payment.html"), "utf8");
assert.ok(paymentHtml.includes('paypal-checkout.js'));
assert.ok(paymentHtml.includes('server'));
assert.ok(!paymentHtml.includes('PAYPAL_CLIENT_SECRET'));

for (const file of [
  "api/paypal/catalog.js",
  "api/paypal/_paypal.js",
  "api/paypal/config.js",
  "api/paypal/create-order.js",
  "api/paypal/capture-order.js",
  "paypal-checkout.js",
  "pages/payment.html"
]) {
  const content = fs.readFileSync(path.join(__dirname, "..", file), "utf8");
  assert.ok(!/BAA[A-Za-z0-9_-]{40,}/.test(content), `${file} appears to contain a PayPal credential value`);
}

console.log(`PASS: ${entries.length} catalog items; no zero prices; server-owned SKU checkout; no credential literals.`);
