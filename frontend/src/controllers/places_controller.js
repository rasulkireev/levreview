import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = [ "name", "address", "phoneNumber", "placeId", "map", "info" ];

  connect() {
    if (typeof(window.google) != "undefined") {
      this.initMap();
    }
  }

  populateForm(
    name,
    address,
    place_id,
    phone_number
  ) {
    this.nameTarget.value = name;
    this.addressTarget.value = address;
    this.phoneNumberTarget.value = phone_number;
    this.placeIdTarget.value = place_id;
  }

  initMap() {
    const map = new window.google.maps.Map(
      this.mapTarget,
      {
        center: { lat: -33.8688, lng: 151.2195 },
        zoom: 13,
      }
    );

    const mapInput = document.getElementById("mapInput");
    const autocomplete = new window.google.maps.places.Autocomplete(mapInput, {
      fields: ["place_id", "geometry", "formatted_address", "name", "formatted_phone_number"],
    });
    autocomplete.bindTo("bounds", map);

    map.controls[window.google.maps.ControlPosition.TOP_LEFT].push(mapInput);

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

      this.populateForm(
        place.name,
        place.formatted_address,
        place.place_id,
        place.formatted_phone_number
      );
    });
  }
}