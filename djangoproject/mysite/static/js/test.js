$(document).ready(function(){
    $('.dot').click(function() {
        var value_pk = $(this).attr('value');
        value_pk = '/basket/add/' + value_pk + '/';
        var path_img = '/media/' + this.id + '.jpg'
        $('#color_image').attr({src: path_img});
        $('.dot').removeClass('active');
        $(this).addClass('active');
        $('form').attr({action: value_pk});
    });
});