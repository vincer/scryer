var up_url = '{{ UP_URL }}';
var down_url = '{{ DOWN_URL }}';

simply.title('scryer');
var processResp = function (data, code) {
   simply.subtitle(code);
};

simply.on('singleClick', function (e) {
   if (e.button === 'up') {
      ajax({ url: up_url, method: 'put' },
            processResp, processResp);
   } else if (e.button === 'down') {
      ajax({ url: down_url, method: 'put' },
            processResp, processResp);
   }
});
