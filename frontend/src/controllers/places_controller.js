import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = [ "name", "address", "phoneNumber", "placeId" ];

  connect() {
    if (typeof(window.google) != "undefined") {
      this.initMap();
    }
  }

  initMap() {
    this.map = new window.google.maps.Map(
      document.getElementById("map"),
      {
        center: { lat: 39.5, lng: -98.35 },
        zoom: 13,
      }
    );

    this.autocomplete = new window.google.maps.places.Autocomplete(this.nameTarget, {
      fields: ["place_id", "geometry", "formatted_address", "name", "formatted_phone_number"],
    });
    this.autocomplete.bindTo("bounds", this.map);
    this.autocomplete.addListener("place_changed", this.placeChanged.bind(this));


    this.marker = new window.google.maps.Marker({
      map: this.map,
      anchorPoint: new window.google.maps.Point(0, -29)
    });
  }

  placeChanged() {
    let place = this.autocomplete.getPlace();

    if (!place.geometry) {
      window.alert(`No details available for input: ${place.name}`);
      return;
    }

    if (place.geometry.viewport) {
      this.map.fitBounds(place.geometry.viewport);
    } else {
      this.map.setCenter(place.geometry.location);
      this.map.setZoom(17);
    }

    this.marker.setPosition(place.geometry.location);
    this.marker.setVisible(true);

    this.nameTarget.value = place.name;
    this.addressTarget.value = place.formatted_address;
    this.phoneNumberTarget.value = place.formatted_phone_number;
    this.placeIdTarget.value = place.place_id;

  }

  keydown(event) {
    if (event.key == "Enter") {
      event.preventDefault();
    }
  }
}