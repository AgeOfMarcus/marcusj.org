---
title: hello world
---
# Obfuscating `hello world`

*The most complicated `hello world` program in a single line.*

After reading [this article](https://benkurtovic.com/2014/06/01/obfuscating-hello-world.html) about obfuscating the classic ***hello world*** program. The author ended up with the following python code:

<pre><code class='python'>
(lambda _, __, ___, ____, _____, ______, _______, ________:
    getattr(
        __import__(True.__class__.__name__[_] + [].__class__.__name__[__]),
        ().__class__.__eq__.__class__.__name__[:__] +
        ().__iter__().__class__.__name__[_____:________]
    )(
        _, (lambda _, __, ___: _(_, __, ___))(
            lambda _, __, ___:
                chr(___ % __) + _(_, __, ___ // __) if ___ else
                (lambda: _).func_code.co_lnotab,
            _ << ________,
            (((_____ << ____) + _) << ((___ << _____) - ___)) + (((((___ << __)
            - _) << ___) + _) << ((_____ << ____) + (_ << _))) + (((_______ <<
            __) - _) << (((((_ << ___) + _)) << ___) + (_ << _))) + (((_______
            << ___) + _) << ((_ << ______) + _)) + (((_______ << ____) - _) <<
            ((_______ << ___))) + (((_ << ____) - _) << ((((___ << __) + _) <<
            __) - _)) - (_______ << ((((___ << __) - _) << __) + _)) + (_______
            << (((((_ << ___) + _)) << __))) - ((((((_ << ___) + _)) << __) +
            _) << ((((___ << __) + _) << _))) + (((_______ << __) - _) <<
            (((((_ << ___) + _)) << _))) + (((___ << ___) + _) << ((_____ <<
            _))) + (_____ << ______) + (_ << ___)
        )
    )
)(
    *(lambda _, __, ___: _(_, __, ___))(
        (lambda _, __, ___:
            [__(___[(lambda: _).func_code.co_nlocals])] +
            _(_, __, ___[(lambda _: _).func_code.co_nlocals:]) if ___ else []
        ),
        lambda _: _.func_code.co_argcount,
        (
            lambda _: _,
            lambda _, __: _,
            lambda _, __, ___: _,
            lambda _, __, ___, ____: _,
            lambda _, __, ___, ____, _____: _,
            lambda _, __, ___, ____, _____, ______: _,
            lambda _, __, ___, ____, _____, ______, _______: _,
            lambda _, __, ___, ____, _____, ______, _______, ________: _
        )
    )
)
</code></pre>

## Here is my own take on the idea, written from scratch in python3

<iframe frameborder='0' src='https://replit.com/@MarcusWeinberger/obf-hello-world-oneline?theme=replitDark&lite=1' class='repl'></iframe>

