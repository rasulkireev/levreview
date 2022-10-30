import "../styles/tailwind.css";

import { Application } from "@hotwired/stimulus";
import { definitionsFromContext } from "@hotwired/stimulus-webpack-helpers";
import Dropdown from 'stimulus-dropdown';
import Reveal from 'stimulus-reveal-controller';
import Popover from 'stimulus-popover';


// Stimulus
const application = Application.start();
const context = require.context("../controllers", true, /\.js$/);
application.load(definitionsFromContext(context));

application.register('dropdown', Dropdown);
application.register('reveal', Reveal);
application.register('popover', Popover);

window.initMap = function (...args) {
  const event = new Event('google-maps-callback', { bubbles: true, cancelable: true });
  event.args = args;
  document.dispatchEvent(event);
};