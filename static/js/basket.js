window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        const targetHref = event.target;
        $.ajax({
                url: '/baskets/basket_edit/' + targetHref.name + '/' + targetHref.value + '/',
                success: function (data) {
                    $('.basket_list').html(data.result)
                }
        });
        event.preventDefault()
    })
}