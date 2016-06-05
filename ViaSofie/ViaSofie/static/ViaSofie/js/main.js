/**
 * Created by Tim on 17/05/2016.
 */

// Source: http://stackoverflow.com/questions/149055/how-can-i-format-numbers-as-money-in-javascript
Number.prototype.formatMoney = function (c, d, t) {
    var n = this,
        c = isNaN(c = Math.abs(c)) ? 2 : c,
        d = d == undefined ? "." : d,
        t = t == undefined ? "," : t,
        s = n < 0 ? "-" : "",
        i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "",
        j = (j = i.length) > 3 ? j % 3 : 0;
    return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};

function makeSlider(elementId, lowerId, upperId, min, max, step, lowerFormattedId, upperFormattedId) {
    // Optionele parameters!
    lowerFormattedId = lowerFormattedId || null;
    upperFormattedId = upperFormattedId || null;

    var nonLinearSlider = document.getElementById(elementId);

    var lowerValue = document.getElementById(lowerId),
        upperValue = document.getElementById(upperId),
        handles = nonLinearSlider.getElementsByClassName('noUi-handle'),
        lowerFormatted = (lowerFormattedId ? document.getElementById(lowerFormattedId) : null),
        upperFormatted = (upperFormattedId ? document.getElementById(upperFormattedId) : null);

    noUiSlider.create(nonLinearSlider, {
        connect: true,
        behaviour: 'tap',
        //start: [start, stop],
        start: [parseInt(lowerValue.value), parseInt(upperValue.value)],
        step: step,
        range: {
            'min': [min],
            'max': [max]
        }
    });

    // Display the slider value and how far the handle moved
    // from the left edge of the slider.
    nonLinearSlider.noUiSlider.on('update', function (values, handle) {
        var tmp = parseInt(values[handle]);
        if (!handle) {
            lowerValue.value = tmp;
            if (lowerFormatted != null) {
                lowerFormatted.innerHTML = tmp.formatMoney(0, '.', ',')
            }
        } else {
            upperValue.value = tmp;
            if (upperFormatted != null) {
                upperFormatted.innerHTML = tmp.formatMoney(0, '.', ',')
            }
        }
    });

    /*
     function changeValue() {
     nonLinearSlider.noUiSlider.set([parseFloat(lowerValue.value), parseFloat(upperValue.value)]);
     }

     lowerValue.oninput = changeValue;
     lowerValue.onpropertychange = changeValue; // for IE8

     upperValue.oninput = changeValue;
     upperValue.onpropertychange = changeValue; // for IE8
     */
}