document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".form-toggle button");
  const forms = document.querySelectorAll(".form-section");

  function showForm(formId, button) {

    forms.forEach(section => section.style.display = "none");
    document.getElementById(formId).style.display = "block";

    buttons.forEach(btn => btn.classList.remove("active"));
    button.classList.add("active");


    if (formId === "mapSection" && window.map) {
      window.map.setCenter(window.mapCenter);
    }
  }

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const formId = button.getAttribute("data-form");
      showForm(formId, button);
    });
  });


  if (buttons.length > 0) {
    buttons[0].click();
  }
});

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");
  const { Marker } = await google.maps.importLibrary("marker");

  window.mapCenter = { lat: 38.9590, lng: -8.5250 };

  window.map = new Map(document.getElementById("map"), {
    zoom: 14,
    center: window.mapCenter,
  });

  fetch("/map-data")
    .then(response => response.json())
    .then(points => {
      points.forEach(p => {
        const marker = new Marker({
          position: { lat: parseFloat(p.lat), lng: parseFloat(p.lng) },
          map: window.map,
          title: p.nome,
        });

        const info = new google.maps.InfoWindow({
          content: `<b>${p.nome}</b><br>Tipo: ${p.tipo}`,
        });

        marker.addListener("click", () => {
          info.open(window.map, marker);
        });
      });
    })
    .catch(err => console.error("Erro a carregar pontos:", err));
}


window.addEventListener("load", initMap);

