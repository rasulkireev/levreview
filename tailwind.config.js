module.exports = {
  content: [
    './templates/**/*.html',
    './foxreview/utils.py',
    './frontend/src/controllers/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
