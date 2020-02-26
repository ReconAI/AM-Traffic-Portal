/*global $*/

function randomStr(len, arr) {
    var ans = '';
    for (var i = len; i > 0; i--) {
        ans +=
            arr[Math.floor(Math.random() * arr.length)];
    }
    return ans;
}

function getNewRTImage() {
    var currentPath = window.location.pathname;
    var randomStr = window.randomStr(20, 'abcdef12345');
    $('.output_place img').attr('src', currentPath + '/realtime?seed=' + randomStr);

}

function mainLoad() {
    //set size of image like in selectBox
    $('.output_place').width($('#image_size')[0].value);

    //handler for size changing
    $('#image_size').change(function(e) {
        var newWidth = e.target.value;
        if (newWidth) {
            $('.output_place').width(newWidth);
        }
    })

    $('#btn_show_rt').click(function() {
        var $btn = $('#btn_show_rt');
        if ($btn.attr('started')){
            window.clearInterval(window.intervalRT);    
            $btn.text('Start RealTime');
            $btn.attr('started', null);
        } else {
            window.intervalRT = setInterval(window.getNewRTImage, 1000);
            $btn.attr('started', true);
            $btn.text('Stop RealTime');
        }
    });
}

$(window.document).ready(mainLoad);
