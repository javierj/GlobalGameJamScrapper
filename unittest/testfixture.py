__author__ = 'Javier'

from bs4 import BeautifulSoup

class MockWebClient():
    def __init__(self, url = None):
        self.count_click = 0
        self.url = url
    def load(self, html):
        self.html = html
    def sourceCode(self):
        return BeautifulSoup(self.html)
    def click(self, url):
        self.count_click += 1


class Fixture:
    def __init__(self):

        self.html = """
          <div class="item-list"><ul>  <li class="views-row views-row-1 views-row-odd views-row-first">
	  <a href="/2014/games/return">
  <div class="game-image">

                      </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">The Return</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">A horror story took place in an island and you are trying to find what happened to your family.</div>      </div>
	  </div>
</a></li>
  <li class="views-row views-row-2 views-row-even">
  <a href="/2014/games/medium">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/good_image.jpg?itok=aZ06vgHQ"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/good_image.jpg?itok=wGmKE4hD"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/good_image.jpg?itok=PGlZqKTB"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/good_image.jpg?itok=1Ifpvyyg"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/good_image.jpg?itok=Bb9X3iuy"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/good_image.jpg?itok=aZ06vgHQ"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/good_image.jpg?itok=9SG4VCaj"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/good_image.jpg?itok=5VOard4X"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/good_image.jpg?itok=uFgRtZFe"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/good_image.jpg?itok=aZ06vgHQ" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Medium</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Medium is a one-player performance-based, interactive game that is meant to be played live with an actor present. It uses no visuals- only sound and touch. The player takes on the role of someone...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-3 views-row-odd"><a href="/2014/games/dreaming-awake">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content">
	<span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/alwake_dream.png?itok=ikhdeehy"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/alwake_dream.png?itok=dhukA9dR"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/alwake_dream.png?itok=hldS5IOk"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/alwake_dream.png?itok=amRNuu6d"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/alwake_dream.png?itok=i44K8ULD"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/alwake_dream.png?itok=ikhdeehy"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/alwake_dream.png?itok=pM5d9coK"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/alwake_dream.png?itok=2-DTOc2f"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/alwake_dream.png?itok=YdGY0Xuy"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/alwake_dream.png?itok=ikhdeehy" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Dreaming Awake</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">A game about a boy who scapes his sad life dreaming. He transformable your reality that you dream to solve many problems. But he can not control what and when are the dreams and when he gets back to...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-4 views-row-even"><a href="/2014/games/dreamer-1">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/feature_9.png?itok=V8b38S_q"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/feature_9.png?itok=QF6tWB1p"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/feature_9.png?itok=JlLUwm3s"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/feature_9.png?itok=9forMyOs"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/feature_9.png?itok=2DW1D7Ca"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/feature_9.png?itok=V8b38S_q"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/feature_9.png?itok=-b_llEdS"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/feature_9.png?itok=Z0-PHa_4"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/feature_9.png?itok=NX_LOOvv"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/feature_9.png?itok=V8b38S_q" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Dreamer</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Sonhos sao
      apenas sonhos, o ser humano tem o poder de torna-los inatingiveis ou fact</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-5 views-row-odd"><a href="/2014/games/halet-i-ruhiye">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/ingame_ss_0.png?itok=bhsiHk-5"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/ingame_ss_0.png?itok=-3OS70nc"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/ingame_ss_0.png?itok=hMz-aJDU"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/ingame_ss_0.png?itok=_ph83IDv"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/ingame_ss_0.png?itok=dzMO_5La"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/ingame_ss_0.png?itok=bhsiHk-5"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/ingame_ss_0.png?itok=U7Ln6TLN"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/ingame_ss_0.png?itok=gXC4Lztx"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/ingame_ss_0.png?itok=rR0dFf3I"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/ingame_ss_0.png?itok=bhsiHk-5" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Halet-i Ruhiye</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Its about one person lost his memory and trying to restore it.</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-6 views-row-even"><a href="/2014/games/eris">
  <div class="game-image">

                      </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Eris</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Gods and titans war.
</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-7 views-row-odd"><a href="/2014/games/alex-carlos">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/ggj_conceito.png?itok=dNQ0ttjl"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/ggj_conceito.png?itok=FUQ8muoV"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/ggj_conceito.png?itok=HzAA5deh"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/ggj_conceito.png?itok=TrrwH3Wn"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/ggj_conceito.png?itok=QCHfHSEH"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/ggj_conceito.png?itok=dNQ0ttjl"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/ggj_conceito.png?itok=5cJTPFee"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/ggj_conceito.png?itok=CnWroO6W"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/ggj_conceito.png?itok=8FPrerzC"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/ggj_conceito.png?itok=dNQ0ttjl" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Alex &amp; Carlos</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">ALEX &amp; CARLOS are two aliens that are very different but so much alike. One day they catch a glimpse of each other and embark in an adventure of friendship and cooperation. Born in different...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-8 views-row-even"><a href="/2014/games/moon-rabbit">
  <div class="game-image">

                      </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Moon Rabbit</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">The moon rabbit and his infinite number of friends are hungry</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-9 views-row-odd"><a href="/2014/games/lifeght">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/omino_giusto_0.jpg?itok=7LrMpwWU"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/omino_giusto_0.jpg?itok=Abrroyh1"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/omino_giusto_0.jpg?itok=_VJQaRh-"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/omino_giusto_0.jpg?itok=E9qO5fq-"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/omino_giusto_0.jpg?itok=EfiNnWdg"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/omino_giusto_0.jpg?itok=7LrMpwWU"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/omino_giusto_0.jpg?itok=xek1wxuA"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/omino_giusto_0.jpg?itok=6bwETaV2"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/omino_giusto_0.jpg?itok=zVYOcyMJ"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/omino_giusto_0.jpg?itok=7LrMpwWU" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">LIFEGHT</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">A little being is living happy and thoughtless in his house with is endless light source when suddenly it breaks and he has to escape worried in a dark world, searching for light to eat using his...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-10 views-row-even"><a href="/2014/games/fairyland1942">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/1_6.jpg?itok=i_aO8XUP"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/1_6.jpg?itok=vLFaXmWG"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/1_6.jpg?itok=jkSeN1Vi"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/1_6.jpg?itok=f7H4CFBS"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/1_6.jpg?itok=hDOrd0Xs"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/1_6.jpg?itok=i_aO8XUP"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/1_6.jpg?itok=U1SxNEaz"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/1_6.jpg?itok=boMCr3hC"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/1_6.jpg?itok=o1iWxYHE"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/1_6.jpg?itok=i_aO8XUP" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Fairyland1942</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">This game takes place at a ghetto in Vilna. You are playing as Yossel, a jewish boy who believes the ghetto is a magical place taken by an evil force. In order to save him, his mother uses his...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-11 views-row-odd"><a href="/2014/games/chromozilla">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=8LJcAZC6"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=ID0c1HGP"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=bKlaYHYg"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=CQbsK21l"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=A52-L4bc"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=8LJcAZC6"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=2adwFBfU"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=dsFI0wEs"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=rPJxoOYG"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/screenshot_2014-01-27_18.30.17.png?itok=8LJcAZC6" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Chromozilla</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Mind-blowing more-frustrating-than-hardcore colorful color-based 2D runner game :D

We are looking forward to read what you think about this! You can send to us your feedback from the following...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-12 views-row-even"><a href="/2014/games/view-fighter">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/viewfighter1.png?itok=VAaJDjCG"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/viewfighter1.png?itok=xrSj3p9Z"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/viewfighter1.png?itok=5rZKJbU6"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/viewfighter1.png?itok=Brcc6h-6"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/viewfighter1.png?itok=wFw4JKkr"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/viewfighter1.png?itok=VAaJDjCG"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/viewfighter1.png?itok=rc13QU9-"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/viewfighter1.png?itok=O4qLQUM7"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/viewfighter1.png?itok=DX7Qghsu"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/viewfighter1.png?itok=VAaJDjCG" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">View Fighter</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">A 2D, 2-Player,  split-screen brawler where you fight for screen space, pushing your portion of the screen further onto your opponents half with every kill. </div>      </div>      </div>
</a></li>
  <li class="views-row views-row-13 views-row-odd"><a href="/2014/games/blink">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/logo_14.jpg?itok=nVzrhS7R"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/logo_14.jpg?itok=IORHBXTh"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/logo_14.jpg?itok=Gizw5OyD"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/logo_14.jpg?itok=WafOKDuh"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/logo_14.jpg?itok=f4i2U36U"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/logo_14.jpg?itok=nVzrhS7R"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/logo_14.jpg?itok=YDwNenya"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/logo_14.jpg?itok=m8JEIgUv"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/logo_14.jpg?itok=IQ-Y0kOj"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/logo_14.jpg?itok=nVzrhS7R" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Blink</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Blink is a puzzle platformer. The goal is to make it to the flag at the end of each level. An eye is visible at the top of the screen in each level, when the eye gets too bloodshot the game is over,...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-14 views-row-even"><a href="/2014/games/jack-ripper">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/jack-the-ripper-cover.jpg?itok=h2UEMjk1"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/jack-the-ripper-cover.jpg?itok=O0N5R3PY"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/jack-the-ripper-cover.jpg?itok=hnWrmQhR"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/jack-the-ripper-cover.jpg?itok=pbG5S1Kk"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/jack-the-ripper-cover.jpg?itok=hCprD-zh"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/jack-the-ripper-cover.jpg?itok=h2UEMjk1"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/jack-the-ripper-cover.jpg?itok=jmX-UyDP"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/jack-the-ripper-cover.jpg?itok=GPJUKo_D"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/jack-the-ripper-cover.jpg?itok=ft_LOi9k"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/jack-the-ripper-cover.jpg?itok=h2UEMjk1" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Jack The Ripper</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Stay hidden! You have to avoid being perceived by the citizens of 1800&#039;s London. Lurk in alley ways until you can make a move. Avoid the police bobbies on patrol.</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-15 views-row-odd"><a href="/2014/games/da-bomb">
  <div class="game-image">

                      </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Da bomb</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Its a game where the player has to choose among three paths , good, evil, or something in between</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-16 views-row-even"><a href="/2014/games/four-norsman-ablokalypse">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/norseman_ss1.jpg?itok=sZ8t8fdw"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/norseman_ss1.jpg?itok=Rw4ClYej"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/norseman_ss1.jpg?itok=nMOWc4Do"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/norseman_ss1.jpg?itok=vO789bc2"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/norseman_ss1.jpg?itok=4NRMMqNq"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/norseman_ss1.jpg?itok=sZ8t8fdw"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/norseman_ss1.jpg?itok=nU05VoFA"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/norseman_ss1.jpg?itok=jp7eTjdD"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/norseman_ss1.jpg?itok=oMw214aS"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/norseman_ss1.jpg?itok=sZ8t8fdw" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">The Four Norsman of the Ablokalypse</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">The Four Norsemen
      of the Ablockalypse is a local

There are 3 different colours your warrior can be and when .</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-17 views-row-odd"><a href="/2014/games/kyojin">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/beauty_shot_final.jpg?itok=fK8996F7"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/beauty_shot_final.jpg?itok=MAuBhgaR"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/beauty_shot_final.jpg?itok=ldDIIVRv"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/beauty_shot_final.jpg?itok=B8fC60cU"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/beauty_shot_final.jpg?itok=VSuLhEq1"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/beauty_shot_final.jpg?itok=fK8996F7"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/beauty_shot_final.jpg?itok=7kVF22Nn"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/beauty_shot_final.jpg?itok=wtioaaeh"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/beauty_shot_final.jpg?itok=Vp2kjJg6"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/beauty_shot_final.jpg?itok=fK8996F7" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">KyoJin</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">N/A</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-18 views-row-even"><a href="/2014/games/rybczynski">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/rybczynski3.png?itok=p-YdJ2ww"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/rybczynski3.png?itok=UwXIfGog"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/rybczynski3.png?itok=T5yVjFSs"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/rybczynski3.png?itok=FFZxO7jm"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/rybczynski3.png?itok=RB9cbKSV"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/rybczynski3.png?itok=p-YdJ2ww"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/rybczynski3.png?itok=vjtZaU9k"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/rybczynski3.png?itok=9Z5bdbRX"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/rybczynski3.png?itok=zVtbUIjo"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/rybczynski3.png?itok=p-YdJ2ww" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Rybczynski</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">&quot;Rybczynski&quot; is a camera maze. You observe your character through a matrix of 16 cameras and try to figure out your way through the labyrinth. Inspired by Zbigniew Rybczynski&#039;s movie...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-19 views-row-odd"><a href="/2014/games/narratoreska">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/menu_27.png?itok=-cvKiyFF"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/menu_27.png?itok=X7tZbIdK"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/menu_27.png?itok=M1b9dem8"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/menu_27.png?itok=HZmR2ca-"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/menu_27.png?itok=_dj4ly2q"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/menu_27.png?itok=-cvKiyFF"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/menu_27.png?itok=s-2SIITv"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/menu_27.png?itok=Cq-E1GQe"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/menu_27.png?itok=DCWGG4gf"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/menu_27.png?itok=-cvKiyFF" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Narratoreska</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Co sie
      sie porwac tej historii,...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-20 views-row-even"><a href="/2014/games/nibiru">
  <div class="game-image">

                      </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">nibiru</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">the adventures of fartalon</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-21 views-row-odd"><a href="/2014/games/hide-beak">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/title_1.jpg?itok=sAI73fKk"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/title_1.jpg?itok=yBdRbu_P"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/title_1.jpg?itok=30oggxwI"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/title_1.jpg?itok=070leOgy"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/title_1.jpg?itok=gzMpbuka"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/title_1.jpg?itok=sAI73fKk"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/title_1.jpg?itok=qr5U2mXB"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/title_1.jpg?itok=bVmPxaoC"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/title_1.jpg?itok=9RBcl3Ia"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/title_1.jpg?itok=sAI73fKk" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Hide &amp; Beak</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">You pl
      ay as a


Controls:
W to...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-22 views-row-even"><a href="/2014/games/joes-game">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/2_5.png?itok=qbSpS0SP"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/2_5.png?itok=hWrVDA5i"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/2_5.png?itok=siJYc25J"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/2_5.png?itok=Qkz_pV3s"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/2_5.png?itok=ji-jr9Hm"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/2_5.png?itok=qbSpS0SP"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/2_5.png?itok=VCUMTYNW"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/2_5.png?itok=ZSZw8lS3"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/2_5.png?itok=-qIXmBDj"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/2_5.png?itok=qbSpS0SP" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Joes Game</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">A puzzle game of affecting perspective.</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-23 views-row-odd"><a href="/2014/games/troll-vs-goblin">
  <div class="game-image">

                      </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Troll VS Goblin</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Troll have to catch the goblin and the goblin have to catch the troll.
The troll play on pc with playstation controller or keyboard.
Goblin play on android device. </div>      </div>      </div>
</a></li>
  <li class="views-row views-row-24 views-row-even"><a href="/2014/games/groundhog-day">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/featured_image_2_0.png?itok=nvUqzzS9"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/featured_image_2_0.png?itok=VwlxjqDL"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/featured_image_2_0.png?itok=4tZO89vg"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/featured_image_2_0.png?itok=OTrD-hL0"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/featured_image_2_0.png?itok=aCz53Jmw"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/featured_image_2_0.png?itok=nvUqzzS9"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/featured_image_2_0.png?itok=iRTNV0-e"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/featured_image_2_0.png?itok=ugDtqGNz"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/featured_image_2_0.png?itok=AjINsqOv"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/featured_image_2_0.png?itok=nvUqzzS9" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Groundhog Day</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">On a small english town, on a rainy night, a mysterious murder happened. You play the game as a detective who, in a Sherlockian way, is running around the town the day after the crime, interrogating...</div>      </div>      </div>
</a></li>
  <li class="views-row views-row-25 views-row-odd views-row-last"><a href="/2014/games/duality-ancients">
  <div class="game-image">

    <div class="views-field views-field-field-game-featured-image">            <div class="field-content"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/loading_screen.png?itok=oSa_uptP"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile/public/game/featured_image/loading_screen.png?itok=xksZPyfx"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__mobile_2x/public/game/featured_image/loading_screen.png?itok=xzpkM3T-"  data-width="100" data-height="71"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow/public/game/featured_image/loading_screen.png?itok=1K0eze_G"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__narrow_2x/public/game/featured_image/loading_screen.png?itok=XB5S_UZW"  data-width="190" data-height="135"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/loading_screen.png?itok=oSa_uptP"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal_2x/public/game/featured_image/loading_screen.png?itok=vzIU4sXG"  data-width="188" data-height="134"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide/public/game/featured_image/loading_screen.png?itok=MnRXXt8V"  data-width="242" data-height="172"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/game_listing__wide_2x/public/game/featured_image/loading_screen.png?itok=i0Mb0168"  data-width="242" data-height="172"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/game_listing__normal/public/game/featured_image/loading_screen.png?itok=oSa_uptP" width="188" height="134" alt="" /></noscript>
</span></div>    </div>  </div>

  <div class="game-content">

      <div class="views-field views-field-title">                <span class="field-content">Duality of The Ancients</span>      </div>
      <div class="views-field views-field-field-game-about">                <div class="field-content">Duality of The Ancients is a 2D platform game.
To complete a level you have to collect all energy orbs.
You can switch between two forms of the spirit you control. Each form can pick up...</div>      </div>      </div>
</a></li>
</ul></div>    </div>

<h2 class="element-invisible">Pages</h2><ul class="pager"><li class="pager__item pager__item--current">1</li>
<li class="pager__item"><a title="Go to page 2" href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=1">2</a></li>
<li class="pager__item"><a title="Go to page 3" href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=2">3</a></li>
<li class="pager__item"><a title="Go to page 4" href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=3">4</a></li>
<li class="pager__item"><a title="Go to page 5" href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=4">5</a></li>
<li class="pager__item"><a title="Go to page 6" href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=5">6</a></li>
<li class="pager__item"><a title="Go to page 7" href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=6">7</a></li>
<li class="pager__item"><a title="Go to page 8" href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=7">8</a></li>
<li class="pager__item"><a title="Go to page 9" href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=8">9</a></li>
<li class="pager__item pager__item--ellipsis"></li>
<li class="pager__item pager__item--next"><a href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=1">Next </a></li>
<li class="pager__item pager__item--last"><a href="/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page=170"></a></li>
</ul>

        """
        self.client = MockWebClient()
        self.client.load(self.html)

        self.gamedetail=u"""

                """