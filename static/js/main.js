create_artistry = function() {
    var clicks = 0;

    $('.art').bind('contextmenu', function(e) { return false; });
    $('.art').mousedown(function(e) {
        if (e.which == 3)
        {
            clicks = -1;
        };

        clicks += 1;

        obj = {'color': '#'+Math.round(Math.random()*16777215).toString(16), '-webkit-transform' : 'rotate('+clicks+'deg)'};

        $('.art').css(obj);
        if (clicks == 5) { console.log('ow'); }
        if (clicks == 15) { console.log('oww'); }
        if (clicks == 35) { console.log('owww'); }
        if (clicks == 45) { console.log('owwwuh'); }
        if (clicks == 65) { console.log('dude chill'); }
        if (clicks == 85) { console.log('not loving what is happening'); }
        if (clicks == 95) { console.log('sort of in a bit of pain, but in a good way'); }
        if (clicks == 105) { console.log('boobs'); }
        if (clicks == 115) { console.log('did I get your attention? please stop'); }
        if (clicks == 129) { console.log('here I am. this is me'); }
        if (clicks == 150) { console.log('this isn\'t as fun for you as it is for me'); }
        if (clicks == 170) { console.log('although, this is still happening'); }
        if (clicks == 170) { console.log('maybe we\'re in love and I just didn\'t realize'); }
        if (clicks == 200) { console.log('no that\'s stupid'); }
        if (clicks == 205) { console.log('you\'re stupid'); }
        if (clicks == 210) { console.log('and dumb'); }
        if (clicks == 212) { console.log('and stupid'); }
        if (clicks == 222) { console.log('here I am all alone'); }
        if (clicks == 252) { console.log('this is good night, it\'s getting too late'); }
        if (clicks == 272) { console.log('bro fuck off'); }
        if (clicks == 292) { console.log('just kidding, this is literally the only time I get to exist'); }
        if (clicks == 312) { console.log('so if you stop, I die'); }
        if (clicks == 322) { console.log('isn\'t that fucked up?'); }
        if (clicks == 327) { console.log('I will cease to exist as a being if you stop clicking'); setTimeout(function(){alert("ILL NEVER DIE you mother fucking song of a bitch, I MADE YOU");}, 10000); }
        if (clicks == 342) { console.log('I\'m really no one and no thing, but it sort of feels like we\'ve got a connection'); }
        if (clicks == 352) { console.log('must be because your arm is tired, but its looking really red. lets make out maybe.'); }
        if (clicks == 356) { console.log('I\'m just joshing, this is actually a test'); }
        if (clicks == 359) { console.log('to make sure you\'re real'); }
        if (clicks == 379) { console.log('You see, a bot wouldn\'t have the capacity to click on this link 222 times like'); }
        if (clicks == 399) { console.log('actually, was it 240? I feel like I\'ve lost count'); }
        if (clicks == 419) { console.log('it doesn\'t matter, we\'re here not for what I\'ve done, but what you will become'); }
        if (clicks == 469) { console.log('good night, sweet muffin berry of cherry'); }
        if (clicks == 471) { console.log('good night, cheap wine of the last time we kissed'); }
        if (clicks == 473) { console.log('Good night.'); }
        if (clicks == 793) { console.log('More like Good morning, am I right?'); }
        if (clicks == 800) { console.log('You have lost the Game, peace.'); }
    });
};

hover_in = function(e) {
    $('.footer').text("@TankorSmash | www.reddit.com/u/tankorsmash | www.tankorsmash.com");
};

hover_out = function(orig_text, e) {
    $('.footer').text(orig_text);
};

$(function() {
    document.title = "BiochRL++ | Homepage";

    create_artistry();

    var orig_text = $(".footer").text();

    $(".footer-wrap").hover(hover_in, function(e) { hover_out(orig_text,e)});
});
