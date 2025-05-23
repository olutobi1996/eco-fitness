$(document).ready(function() {
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    $('.qty_input').each(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    $('.increment-qty').click(function(e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input');
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1).trigger('change');
    });

    $('.decrement-qty').click(function(e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input');
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1).trigger('change');
    });
});
