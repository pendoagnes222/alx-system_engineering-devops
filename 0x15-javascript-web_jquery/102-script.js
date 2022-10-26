$(document).ready(function () {
  $('#btn_search').on('click', function () {
    let cityName = $('#city_search').val();
    $('#city_search').val('');

    let url = '(https://www.fourtonfish.com/hellosalut/hello/'+ cityName + '%22)&format=json';

    $.get(url, (data) => {
      $('DIV#hello').text(data.query.results.channel.hello);
    });
  });
});

