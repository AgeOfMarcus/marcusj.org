_auto = true;
_proj_index = 0;
_blinking = true;
_max_input_time = 3000;
_max_time_per_character = 250;
_img_index = 0;

fetch('/commands').then(r => {
    r.json().then(res => {
        globalThis.commands = res.commands;
    })
})

fetch('/projects').then(r => {
    r.json().then(res => {
        globalThis.projects = res.projects;
    })
})

function typewrite(text, callback) {
    if (globalThis._tw) {
        clearInterval(_tw);
    }
    $('#input').val('');

    elm = $('#input');
    $('.ps1').text($('.ps1').text().replace('|',''));
    _blinking = false;
    tpc = _max_time_per_character;
    if ((tpc * text.length) > _max_input_time) {
        tpc = _max_input_time / text.length;
    }

    globalThis._tw = setInterval(function() {
        if (elm.val() == text) {
            setTimeout(function() {
                _blinking = true;
                callback();
            }, tpc*2)
            clearInterval(_tw);
            _tw = false;
        } else {
            elm.val(elm.val() + text[elm.val().length])
        }
    }, tpc);
}

function cycle(increment=1) {
    _proj_index = _proj_index + increment;
    if (_proj_index > (projects.length - 1)) {
        _proj_index = 0;
    }
    if (_proj_index < 0) {
        _proj_index = projects.length - 1;
    }
    proj = projects[_proj_index];
    if (!proj.title) {
        return cycle(0);
    }
    typewrite(proj.title, function() {
        $('#output').html(proj.body);
        document.querySelectorAll('pre code').forEach((block) => {
            hljs.highlightElement(block);
        });
    })
    /*
    $('w3-content').empty();
    proj.images.forEach((image, index) => {
        $('.w3-content').append($(`<img src='${image}' class='image'></img>`));
    });
    globalThis._img_index = 0;
    */
}

function cycleImg(increment=1) {
    _img_index = _img_index + increment;
    images = $('.w3-content')[0].childNodes;
    if (_img_index > (images.length - 1)) {
        _img_index = 0;
    }
    if (_img_index < 0) {
        _img_index = images.length - 1;
    }

    $('.image').css('display', 'none')
    images[_img_index].style.display = 'block';
}

/*
function toggleAutoplay() {
    _auto = !_auto;
    $('#autoplay').css('background-color', _auto ? 'green' : 'rgb(42, 97, 42)');
}

setInterval(function() {
    if (_auto) {
        cycle();
    }
}, 7000)
*/

// caret
setInterval(function() {
    if (_blinking) {
        if ($('.ps1').text().endsWith('|')) {
            $('.ps1').text($('.ps1').text().replace('|',''));
        } else {
            $('.ps1').text($('.ps1').text() + '|');
        }
    }
}, 600)

$('button.left').hover(
    function() {
        $(this).text('<<');
    },
    function() {
        $(this).text("<");
    }
)

$('button.right').hover(
    function() {
        $(this).text('>>');
    },
    function() {
        $(this).text(">");
    }
)