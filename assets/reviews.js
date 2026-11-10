/* Live Google rating and review count. The reviews themselves are chosen by the salon. */
const GOOGLE_REVIEWS = { key: "AIzaSyDi8_w6A9v8WE134_ZMd9xmP0J1b-6R2IQ", placeId: "ChIJ20pzclP3t4kRW6qnVT1pZXM" };

(function () {
  const cfg = GOOGLE_REVIEWS;
  const section = document.getElementById("reviews");
  if (!cfg.key || !cfg.placeId || !section) return;

  function loadMaps() {
    (g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({ key: cfg.key, v: "weekly" });
  }

  async function run() {
    try {
      loadMaps();
      const { Place } = await google.maps.importLibrary("places");
      const place = new Place({ id: cfg.placeId });
      await place.fetchFields({ fields: ["rating", "userRatingCount", "googleMapsURI"] });
      if (place.rating) document.getElementById("rv-rating").textContent = place.rating.toFixed(1);
      if (place.userRatingCount) document.getElementById("rv-count").textContent = place.userRatingCount.toLocaleString() + " Google reviews";
      if (place.googleMapsURI) {
        document.getElementById("rv-link").href = place.googleMapsURI;
        document.getElementById("rv-all").href = place.googleMapsURI;
      }
    } catch (err) {
      console.warn("Google rating could not load; showing the saved count.", err);
    }
  }

  // Ask Google only when a visitor gets near the reviews, to keep calls low.
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(entries => {
      if (entries.some(e => e.isIntersecting)) { io.disconnect(); run(); }
    }, { rootMargin: "600px 0px" });
    io.observe(section);
  } else {
    run();
  }
})();
