__author__ = 'Javier'

from bs4 import BeautifulSoup

class MockWebClient():
    def __init__(self, url = "MockURL"):
        self.count_click = 0
        self.url = url
    def load(self, html):
        self.html = html
    def sourceCode(self):
        return BeautifulSoup(self.html)
    def click(self, url):
        self.count_click += 1
    def setUrl(self, nexturl):
        pass


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
<body class="html not-front not-logged-in no-sidebars page-node page-node- page-node-5108 node-type-game section-2014">
  <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
    <div class="l-page">
  <header class="l-header" role="banner">
    <div class="l-header--inner">
      <div class="logo"></div>
        <div class="l-region l-region--header">
    <div id="block-delta-blocks-site-name" class="block block--delta-blocks block--delta-blocks-site-name">
        <div class="block__content">
    <h2 class="site-name"><a href="/" title="Return to the Global Game Jam home page"><span>Global Game Jam</span></a></h2>  </div>
</div>
<div id="block-delta-blocks-site-slogan" class="block block--delta-blocks block--delta-blocks-site-slogan">
        <div class="block__content">
    <h6 class="site-slogan">24 26 January 2014</h6>  </div>
</div>
  </div>
        <div class="l-region l-region--navigation">
    <div id="block-search-form" role="search" class="block block--search block--search-form">
        <div class="block__content">
    <form class="search-form search-block-form" action="/2014/games/return" method="post" id="search-block-form" accept-charset="UTF-8"><div><div class="container-inline">
      <h2 class="element-invisible">Search form</h2>
    <div class="form-item form-type-textfield form-item-search-block-form">
  <input title="Enter the terms you wish to search for." placeholder="Search" class="custom-search-box form-text" type="text" id="edit-search-block-form--2" name="search_block_form" value="" size="15" maxlength="128" />
</div>
<div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit" name="op" value="Search" class="form-submit" /></div><input type="hidden" name="form_build_id" value="form-b4D0mKY7jlb2LGV0J8oF5N-T49pHFkdvmCmOGVRRp3A" />
<input type="hidden" name="form_id" value="search_block_form" />
</div>
</div></form>  </div>
</div>
<nav id="block-system-main-menu" role="navigation" class="block block--system block--menu block--system-main-menu">

  <ul class="menu"><li class="first leaf"><a href="/about">About</a></li>
<li class="leaf"><a href="/faq">FAQ</a></li>
<li class="leaf"><a href="/2014/games" title="">Games</a></li>
<li class="last leaf"><a href="/jam-sites" title="">Locations</a></li>
</ul></nav>
  </div>
    </div>
    <div class="l-user-links">
      <div class="l-user-links--inner">
          <div class="l-region l-region--user-links">
    <div id="block-user-login" role="form" class="block block--user block--user-login">
        <h2 class="block__title">Log in</h2>
      <div class="block__content">
    <div class="column drupal-login">
      <form class="user-login-form" action="/2014/games/return?destination=node/5108" method="post" id="user-login-form" accept-charset="UTF-8"><div><div class="form-item form-type-textfield form-item-name">
 <input placeholder="Username" type="text" id="edit-name" name="name" value="" size="15" maxlength="60" class="form-text required" />
</div>
<div class="form-item form-type-password form-item-pass">
 <input placeholder="Password" type="password" id="edit-pass" name="pass" size="15" maxlength="128" class="form-text required" />
</div>
<input type="hidden" name="form_build_id" value="form-q1Sixz0dGpvySxd3KgDO-B9bVZ0KtUbU3dYB2rE3KzA" />
<input type="hidden" name="form_id" value="user_login_block" />
<div class="form-actions form-wrapper" id="edit-actions--2"><input type="submit" id="edit-submit--2" name="op" value="Log in" class="form-submit" /></div></div></form>    </div>
    <div class="column fb-login">
      <p>Connect with:</p><a href="https://www.facebook.com/dialog/oauth?client_id=620875854629299&amp;redirect_uri=http%3A//globalgamejam.org/fboauth/connect&amp;scope=email"><span class="fb-button">Facebook</span></a>    </div>
    <div class="login-footer">
      <div class="column">
        <a href="/user/password" class="request-password">Forgot password?</a>      </div>
      <div class="column sign-up">
        <p>Don't have an account yet?</p> <a href='/user/signup/to'>Sign up</a>      </div>
    </div>
  </div>
</div>
  </div>
      </div>
    </div>
  </header>

  <div class="l-intro">
      </div>

  <a id="main-content"></a>
  <div class="l-main">
    <div class="l-content" role="main">
                          <h1>The Return</h1>
                                    <div class="l-content--inner">
        <article about="/2014/games/return" typeof="sioc:Item foaf:Document" role="article" class="node node--game node--full node--game--full">

  <div class="featured-image">
          <div id="block-views-games-featured-image-block" class="block block--views block--views-games-featured-image-block">
        <div class="block__content">
    <div class="view view-games view-id-games view-display-id-featured_image_block view-dom-id-2c1b331008330846daa4c1814f58f86c">



      <div class="view-content">
      <div class="item-list"><ul>  <li class="views-row views-row-1 views-row-odd views-row-first views-row-last"></li>
</ul></div>    </div>






</div>  </div>
</div>
      </div>

  <div class="node__content">
    <div class="links">
          </div>

    <div class="field field--name-field-game-about field--type-text-long field--label-hidden">
	<div class="field__items">
	<div class="field__item even">A horror story took place in an island and you are trying to find what happened to your family.</div></div></div><div class="field field--name-og-group-ref field--type-entityreference field--label-inline clearfix"><div class="field__label">Jam Site:&nbsp;</div><div class="field__items"><div class="field__item even"><a href="http://globalgamejam.org/2014/jam-sites/iran-game-development-institute">Iran Game Development Institute</a></div></div></div><div class="field field--name-field-game-year field--type-entityreference field--label-inline clearfix"><div class="field__label">Jam year:&nbsp;</div><div class="field__items"><div class="field__item even"><a href="/2014/jam-sites">2014</a></div></div></div><div class="field field--name-field-game-platforms field--type-list-text field--label-inline clearfix"><div class="field__label">Platforms:&nbsp;</div><div class="field__items"><div class="field__item even"><div class="textformatter-list">MS Windows</div></div></div></div><div class="field field--name-field-game-tools field--type-list-text field--label-inline clearfix">

	<div class="field__label">Tools and Technologies:&nbsp;</div>
	<div class="field__items">
	<div class="field__item even">
	<div class="textformatter-list">Unity (any product)</div></div></div></div>
	<div class="field field--name-field-game-source-files field--type-file field--label-inline clearfix"><div class="field__label">Source files:&nbsp;</div><div class="field__items"><div class="field__item even"><span class="file"><img class="file-icon" alt="" title="application/zip" src="/modules/file/icons/package-x-generic.png" /> <a href="http://ggj.s3.amazonaws.com/games/2014/01/27/2300/The-Return_Source.zip" type="application/zip; length=0">The-Return_Source.zip</a></span></div></div></div><div class="field field--name-field-game-executable field--type-file field--label-inline clearfix"><div class="field__label">Executable:&nbsp;</div><div class="field__items"><div class="field__item even"><span class="file"><img class="file-icon" alt="" title="application/zip" src="/modules/file/icons/package-x-generic.png" /> <a href="http://ggj.s3.amazonaws.com/games/2014/01/27/2301/The_Return.zip" type="application/zip; length=0">The_Return.zip</a></span></div></div></div>  </div>

  <div class="game-sidebar">
          <div class="team">
        <h3>Team</h3>
        <div class="team-image">
                      <div id="block-views-games-team-image-block" class="block block--views block--views-games-team-image-block">
        <div class="block__content">
    <div class="view view-games view-id-games view-display-id-team_image_block view-dom-id-1576cbd1257fb0c5c1c7d0dff03d5c91">



      <div class="view-content">
      <div class="item-list"><ul>  <li class="views-row views-row-1 views-row-odd views-row-first views-row-last"></li>
</ul></div>    </div>






</div>  </div>
</div>
                  </div>
        <div class="team-members">
                      <div id="block-views-game-users-team-block" class="block block--views block--views-game-users-team-block">
        <div class="block__content">
    <div class="view view-game-users view-id-game_users view-display-id-team_block view-dom-id-0b10e35136759baec73b49faf165a59c">



      <div class="view-content">
      <div class="item-list"><ul>  <li class="views-row views-row-1 views-row-odd views-row-first views-row-last">
  <div class="views-field views-field-field-user-image">        <div class="field-content"><a href="/users/amir-badamchi"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__normal/public/user/amir.jpg?itok=x9KPmsuX"  data-width="56" data-height="56"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__narrow/public/user/amir.jpg?itok=dyWR4Elg"  data-width="42" data-height="42"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__narrow_2x/public/user/amir.jpg?itok=ZT-3RVG0"  data-width="42" data-height="42"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__narrow/public/user/amir.jpg?itok=dyWR4Elg"  data-width="42" data-height="42"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__narrow_2x/public/user/amir.jpg?itok=ZT-3RVG0"  data-width="42" data-height="42"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__normal/public/user/amir.jpg?itok=x9KPmsuX"  data-width="56" data-height="56"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__normal_2x/public/user/amir.jpg?itok=ajp2NKre"  data-width="56" data-height="56"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__wide/public/user/amir.jpg?itok=2oDl7QL8"  data-width="70" data-height="70"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__wide_2x/public/user/amir.jpg?itok=QXgYG_MU"  data-width="70" data-height="70"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/user_profile_picture__normal/public/user/amir.jpg?itok=x9KPmsuX" width="56" height="56" alt="" /></noscript>
</span></a></div>  </div>
  <div class="views-field views-field-name">        <span class="field-content"><a href="/users/amir-badamchi" title="View user profile." class="username">Amir Badamchi</a></span>  </div>
<div class="administrative-links">
  </div>
</li>
</ul></div>    </div>






</div>  </div>
</div>
            <div class="game-add-jammers clearfix">
                          </div>
                  </div>
      </div>
      </div>
</article>
      </div>
          </div>

          </div>

  <footer class="l-footer" role="contentinfo">
      <div class="l-region l-region--footer">
    <div id="block-views-sponsors-major-block" class="block block--views block--views-sponsors-major-block">
        <div class="block__content">
    <div class="view view-sponsors view-id-sponsors view-display-id-major_block view-dom-id-8fd7c3aff680eca6af5362936e7b0bd4">


  <li class="views-row views-row-2 views-row-even views-row-last">
  <div class="views-field views-field-field-sponsor-logo">        <div class="field-content"><a href="http://www.gamesprout.com" target="_blank"><span data-picture="">
<span data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__normal/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=-0yVyJh-"  data-width="128" data-height="64"></span>
<span data-media="(min-width: 0)" data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__default/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=rjxg58-Y"  data-width="100%"></span>
<span data-media="(min-width: 0) and (min-device-pixel-ratio: 2), (min-width: 0) and (-o-min-device-pixel-ratio: 2), (min-width: 0) and (-webkit-min-device-pixel-ratio: 2), (min-width: 0) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__default_2x/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=f-8nfjkc"  data-width="100%"></span>
<span data-media="(min-width: 740px)" data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__narrow/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=KrJcSVj-"  data-width="152" data-height="76"></span>
<span data-media="(min-width: 740px) and (min-device-pixel-ratio: 2), (min-width: 740px) and (-o-min-device-pixel-ratio: 2), (min-width: 740px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 740px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__narrow_2x/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=DrHKwRbl"  data-width="152" data-height="76"></span>
<span data-media="(min-width: 980px)" data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__normal/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=-0yVyJh-"  data-width="128" data-height="64"></span>
<span data-media="(min-width: 980px) and (min-device-pixel-ratio: 2), (min-width: 980px) and (-o-min-device-pixel-ratio: 2), (min-width: 980px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 980px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__normal_2x/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=_QIvju3Z"  data-width="128" data-height="64"></span>
<span data-media="(min-width: 1220px)" data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__wide/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=hXTJnric"  data-width="164" data-height="82"></span>
<span data-media="(min-width: 1220px) and (min-device-pixel-ratio: 2), (min-width: 1220px) and (-o-min-device-pixel-ratio: 2), (min-width: 1220px) and (-webkit-min-device-pixel-ratio: 2), (min-width: 1220px) and (min-resolution: 2dppx)" data-src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__wide_2x/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=Qo7DaFLH"  data-width="164" data-height="82"></span>
<noscript><img typeof="foaf:Image" src="http://globalgamejam.org/sites/default/files/styles/sponsor_logo__normal/public/GameSprout%20Logo%20%28710x223%29%20White%20Background.jpg?itok=-0yVyJh-" width="128" height="64" alt="" /></noscript>
</span></a></div>  </div></li>
</ul></div>    </div>


</div>  </div>
</div>
<div id="block-views-sponsors-additional-block" class="block block--views block--views-sponsors-additional-block">
        <div class="block__content">
    <div class="view view-sponsors view-id-sponsors view-display-id-additional_block view-dom-id-16dbed44ea785dca3bae49cd6327b128">

</div>  </div>
</div>
<div id="block-boxes-footer-links" class="block block--boxes block-boxes-simple block--boxes-footer-links">
        <div class="block__content">
    <div id='boxes-box-footer_links' class='boxes-box'><div class="boxes-box-content"><ul><li><a href="/contact" rel="nofollow">Contact</a></li>
<li><a href="/press" rel="nofollow">Press</a></li>
<li><a href="/research" rel="nofollow">Research</a></li>
<li><a href="/legal" rel="nofollow">Legal</a></li>
<li><a href="/sponsors" rel="nofollow">Sponsors</a></li>
<li><a class="twitter social-media" href="http://twitter.com/globalgamejam" rel="nofollow"><span class="icon">Twitter</span></a></li>
<li><a class="facebook social-media" href="https://facebook.com/GlobalGameJam" rel="nofollow"><span class="icon">Facebook</span></a></li>
<li><a class="flickr social-media" href="http://www.flickr.com/groups/ggj13/" rel="nofollow"><span class="icon">Flickr</span></a></li>
<li><a class="gplus social-media" href="http://plus.google.com/+GlobalGameJam" rel="nofollow"><span class="icon">Google Plus</span></a></li>
<li><a class="pinterest social-media" href="http://pinterest.com/globalgamejam/" rel="nofollow"><span class="icon">Pinterest</span></a></li>
<li><a class="tumblr social-media" href="http://jamtales.tumblr.com" rel="nofollow"><span class="icon">Tumblr</span></a></li>
<li><a class="vimeo social-media" href="http://vimeo.com/globalgamejam" rel="nofollow"><span class="icon">Vimeo</span></a></li>
<li><a class="youtube social-media" href="http://www.youtube.com/user/GlobalGameJam" rel="nofollow"><span class="icon">YouTube</span></a></li>
</ul></div></div>  </div>
</div>

  <script src="http://globalgamejam.org/sites/default/files/js/js_3wrGQPDBQybctdh-2ZAYgDxvLTXELT4x2_Nl9oWyhNQ.js"></script>
</body>

                """
        self.gameclient = MockWebClient()
        self.gameclient.load(self.gamedetail)