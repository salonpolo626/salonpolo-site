/* Salon Polo: count taps on Book, Call and Directions so Google Ads can see them. */
(function () {
  var staff = {
    "8HZcPC7pnCw_wKK3vLH13w": "Alexis",
    "X1TsNiO8WNYVHWTYorO8gQ": "Amber",
    "4P5LVSoCJaKDknl80Vjzyg": "Colette",
    "kJTIY_2ESmKxqZ6ShLrVsw": "Henry"
  };
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a || typeof window.gtag !== "function") return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("phorest.com") !== -1) {
      var m = href.match(/staffId=([^&]+)/);
      window.gtag("event", "book_click", {
        stylist: m ? (staff[m[1]] || "other") : "any",
        page_location: location.href
      });
    } else if (href.indexOf("tel:") === 0) {
      window.gtag("event", "call_click", { page_location: location.href });
    } else if (href.indexOf("google.com/maps") !== -1 || href.indexOf("maps.app.goo.gl") !== -1) {
      window.gtag("event", "directions_click", { page_location: location.href });
    }
  });
})();
