$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').append(data.hello);
  });
});
