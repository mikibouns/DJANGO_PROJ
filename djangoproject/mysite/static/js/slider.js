$(document).ready(function(){
    $('.dot').click(function() {
        var value_pk = $(this).attr('value');
        value_pk = '/basket/add/' + value_pk + '/';
        $('#color_image').attr({src: this.id});
        $('.dot').removeClass('active');
        $(this).addClass('active');
        $('form').attr({action: value_pk});
    });
});