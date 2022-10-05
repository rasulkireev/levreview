import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = [ "field", "map", "info" ];
  connect() {
    if (typeof(window.google) != "undefined") {
      this.initMap();
    }
  }

  initMap() {
    const map = new window.google.maps.Map(
      this.mapTarget,
      {
        center: { lat: -33.8688, lng: 151.2195 },
        zoom: 13,
      }
    );

    const autocomplete = new window.google.maps.places.Autocomplete(this.fieldTarget, {
      fields: ["place_id", "geometry", "formatted_address", "name"],
    });
    autocomplete.bindTo("bounds", map);

    map.controls[window.google.maps.ControlPosition.TOP_LEFT].push(this.fieldTarget);

    const infowindow = new window.google.maps.InfoWindow();
    const infowindowContent = this.infoTarget;
    infowindow.setContent(infowindowContent);

    const marker = new window.google.maps.Marker({ map: map });
    marker.addListener("click", () => {
      infowindow.open(map, marker);
    });

    autocomplete.addListener("place_changed", () => {
      infowindow.close();

      const place = autocomplete.getPlace();

      if (!place.geometry || !place.geometry.location) {
        return;
      }

      if (place.geometry.viewport) {
        map.fitBounds(place.geometry.viewport);
      } else {
        map.setCenter(place.geometry.location);
        map.setZoom(17);
      }

      // Set the position of the marker using the place ID and location.
      // @ts-ignore This should be in @typings/googlemaps.
      marker.setPlace({
        placeId: place.place_id,
        location: place.geometry.location,
      });

      marker.setVisible(true);

      (
        infowindowContent.children.namedItem("place-name")
      ).textContent = place.name;
      (
        infowindowContent.children.namedItem("place-id")
      ).textContent = place.place_id;
      (
        infowindowContent.children.namedItem("place-address")
      ).textContent = place.formatted_address;
      infowindow.open(map, marker);
    });
  }
}