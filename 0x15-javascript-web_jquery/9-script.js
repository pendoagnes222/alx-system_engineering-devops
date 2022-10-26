const url = 'ttps://fourtonfish.com/hellosalut/?lang=fr';

$.get(url, (data) => {
  $('DIV#hello').text(data.query.results.channel.hello);
});
