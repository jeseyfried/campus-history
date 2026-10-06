---
title: UNM Campus Histories
date: 2019-04-25
layout: wide
css: home.css
header-image: "/assets/images/hodgin-sandias-background.jpg"
header-title: UNM Campus Histories
header-subtitle: a student-driven digital history collaboration
header-caption: Hodgin Hall and the Sandia Mountains
header-position: 0px 0px
category: Digital History
---

{% assign essays = site.pages | where_exp: "page", "page.path contains 'essays/'" | where: "name", "index.md" | sort: "title" %}

{% comment %}
  Which essays appear in the Featured and Recommended blocks is curated in
  _data/homepage.yml by folder name. See that file for the rationale.

  Liquid has no lookup-by-key, so each slug is resolved by scanning `essays`
  for a matching folder. Both sides are downcased so a capitalised folder like
  essays/University-Police/ still matches a lowercase entry in the data file.
{% endcomment %}

{% assign featured = nil %}
{% capture feature_json %}
[
{% assign feature_count = 0 %}
{% for slug in site.data.homepage.featured %}
  {% assign slug_norm = slug | downcase %}
  {% assign item = nil %}
  {% for candidate in essays %}
    {% assign candidate_folder = candidate.url | split: '/' | slice: 2, 1 | first | downcase %}
    {% if candidate_folder == slug_norm %}
      {% assign item = candidate %}
      {% break %}
    {% endif %}
  {% endfor %}
  {% if item and item.title and item.card-description and item.card-image %}
    {% comment %}
      Store root-relative paths here, with no baseurl. The script below prepends
      site.baseurl when it swaps in a random essay, so running these through
      relative_url would duplicate the baseurl in production.
    {% endcomment %}
    {% assign card_image = item.card-image | strip %}
    {% unless card_image contains '://' %}
      {% assign card_image_first = card_image | slice: 0, 1 %}
      {% if card_image_first != '/' %}{% assign card_image = card_image | prepend: '/' %}{% endif %}
    {% endunless %}
    {% if feature_count > 0 %},{% endif %}
    {
      "title": {{ item.title | jsonify }},
      "category": {{ item.category | default: "Campus History" | jsonify }},
      "description": {{ item.popup-teaser | default: item.card-description | jsonify }},
      "url": {{ item.url | jsonify }},
      "image": {{ card_image | jsonify }}
    }
    {% assign feature_count = feature_count | plus: 1 %}
    {% comment %} First resolved entry is the pre-JavaScript default. {% endcomment %}
    {% unless featured %}{% assign featured = item %}{% endunless %}
  {% endif %}
{% endfor %}
]
{% endcapture %}
{% assign category_list = "Academic Building|Classroom Building|Dormitory|Historic Building|Landscape|Museum|Office|Public Art|Student Resource|Arts Venue|Campus Services|Dining" | split: "|" %}

<div class="home-magazine">
  <section class="home-deck" aria-labelledby="home-deck-title">
    <div class="home-deck__lead">
      <h2 id="home-deck-title">Spaces have histories, too.</h2>
      <p>UNM Campus Histories collects student-built essays about the buildings, landscapes, public art, and everyday places that shape university life. The project tries to make history more visible.</p>
      <div class="home-actions" aria-label="Homepage links">
        <a class="home-button home-button--quiet" href="{{ '/all-essays/' | relative_url }}">Browse by Name</a>
        <a class="home-button home-button--quiet" href="{{ '/directory/' | relative_url }}">Browse by Category</a>
        <a class="home-button home-button--quiet" href="{{ '/map/' | relative_url }}">Explore the Map</a>
      </div>
    </div>

    <aside class="home-quote" aria-labelledby="home-quote-title" data-home-quotes="{{ site.data.home_quotes | jsonify | escape }}">
      <a class="home-quote__image" data-quote-link href="{{ site.data.home_quotes[0].url | relative_url }}">
        <img data-quote-image src="{{ site.data.home_quotes[0].image | relative_url }}" alt="">
      </a>
      <div class="home-quote__body">
        <p class="home-kicker" id="home-quote-title">From the Essays</p>
        <blockquote>
          <p data-quote-text>{{ site.data.home_quotes[0].text }}</p>
        </blockquote>
        <p class="home-quote__credit">
          <a data-quote-link href="{{ site.data.home_quotes[0].url | relative_url }}"><span data-quote-essay>{{ site.data.home_quotes[0].essay }}</span></a>
          <span data-quote-author>{{ site.data.home_quotes[0].author }}</span>
        </p>
      </div>
      <button class="home-quote__button" type="button" data-quote-next>Another quote</button>
    </aside>
  </section>

  {% if featured %}
  <section class="home-feature" aria-labelledby="featured-story" data-featured-essays="{{ feature_json | strip_newlines | escape }}">
    <a class="home-feature__image" data-feature-link href="{{ featured.url | relative_url }}">
      <img data-feature-image src="{% include images/image-path.html image-path=featured.card-image %}" alt="">
    </a>
    <div class="home-feature__story">
      <p class="home-kicker">Featured Essay <span data-feature-category>{{ featured.category }}</span></p>
      <h2 id="featured-story"><a data-feature-title data-feature-link href="{{ featured.url | relative_url }}">{{ featured.title }}</a></h2>
      <p data-feature-description>{{ featured.popup-teaser | default: featured.card-description }}</p>
      <a class="home-text-link" data-feature-link href="{{ featured.url | relative_url }}">Read the essay</a>
    </div>
  </section>
  {% endif %}


  <section class="home-index" aria-labelledby="strong-work">
    <div class="home-section-heading">
      <p class="home-kicker">Curated Reading</p>
      <h2 id="strong-work">Recommended Essays</h2>
    </div>
    <div class="home-essay-list">
      {% comment %} Curated, in order, in _data/homepage.yml. {% endcomment %}
      {% for slug in site.data.homepage.recommended %}
        {% assign slug_norm = slug | downcase %}
        {% assign essay = nil %}
        {% for candidate in essays %}
          {% assign candidate_folder = candidate.url | split: '/' | slice: 2, 1 | first | downcase %}
          {% if candidate_folder == slug_norm %}
            {% assign essay = candidate %}
            {% break %}
          {% endif %}
        {% endfor %}
        {% if essay and essay.card-description and essay.card-image %}
        <article class="home-essay-row">
          <a href="{{ essay.url | relative_url }}">
            {% if essay.card-image %}
            <img src="{% include images/image-path.html image-path=essay.card-image %}" alt="">
            {% endif %}
            <span>
              <span class="home-essay-row__category">{{ essay.category | default: "Campus History" }}</span>
              <strong>{{ essay.title }}</strong>
              <em>{{ essay.card-description }}</em>
            </span>
          </a>
        </article>
        {% endif %}
      {% endfor %}
    </div>
    <p class="home-index__more"><a class="home-text-link" href="{{ '/all-essays/' | relative_url }}">View all essays by name</a></p>
  </section>
  <section class="home-about" aria-labelledby="home-about-title">
    <div>
      <p class="home-kicker">About the Project</p>
      <h2 id="home-about-title">A public archive of student research</h2>
    </div>
    <p>Campus Histories turns explorations of UNM's official archive into a shared record of UNM's buildings, landscapes, public art, and everyday places. The project asks students to collaborate on a digital project that can keeps circulating long after the semester ends.</p>
    <a class="home-text-link" href="{{ '/about/' | relative_url }}">Read about the project</a>
  </section>

  <section class="home-categories" aria-labelledby="home-categories-title">
    <div class="home-section-heading">
      <p class="home-kicker">Browse the Collection</p>
      <h2 id="home-categories-title">Read by place type</h2>
    </div>
    <div class="home-category-strip">
      {% for category in category_list %}
        {% assign category_essays = essays | where: "category", category %}
        {% if category_essays.size > 0 %}
        <a class="home-category" href="{{ '/directory/' | relative_url }}#{{ category | slugify }}">
          <span>{{ category }}</span>
          <strong>{{ category_essays.size }}</strong>
        </a>
        {% endif %}
      {% endfor %}
    </div>
  </section>
</div>

<script>
(function() {
  function parseData(el, attribute) {
    try {
      return JSON.parse(el.getAttribute(attribute)) || [];
    } catch (error) {
      return [];
    }
  }

  function setLinks(links, href) {
    links.forEach(function(link) {
      link.href = '{{ site.baseurl }}' + href;
    });
  }

  var quoteModule = document.querySelector('[data-home-quotes]');
  if (quoteModule) {
    var quotes = parseData(quoteModule, 'data-home-quotes');
    var quoteText = quoteModule.querySelector('[data-quote-text]');
    var quoteEssay = quoteModule.querySelector('[data-quote-essay]');
    var quoteAuthor = quoteModule.querySelector('[data-quote-author]');
    var quoteImage = quoteModule.querySelector('[data-quote-image]');
    var quoteLinks = quoteModule.querySelectorAll('[data-quote-link]');
    var next = quoteModule.querySelector('[data-quote-next]');
    var currentQuote = Math.floor(Math.random() * quotes.length);

    function showQuote(index) {
      var quote = quotes[index];
      if (!quote) return;
      quoteText.textContent = quote.text;
      quoteEssay.textContent = quote.essay;
      quoteAuthor.textContent = quote.author;
      if (quoteImage && quote.image) quoteImage.src = '{{ site.baseurl }}' + quote.image;
      setLinks(quoteLinks, quote.url);
    }

    showQuote(currentQuote);

    if (next) {
      next.addEventListener('click', function() {
        currentQuote = (currentQuote + 1) % quotes.length;
        showQuote(currentQuote);
      });
    }
  }

  var featureModule = document.querySelector('[data-featured-essays]');
  if (featureModule) {
    var features = parseData(featureModule, 'data-featured-essays');
    var feature = features[Math.floor(Math.random() * features.length)];
    var featureImage = featureModule.querySelector('[data-feature-image]');
    var featureTitle = featureModule.querySelector('[data-feature-title]');
    var featureCategory = featureModule.querySelector('[data-feature-category]');
    var featureDescription = featureModule.querySelector('[data-feature-description]');
    var featureLinks = featureModule.querySelectorAll('[data-feature-link]');

    if (feature) {
      if (featureImage) featureImage.src = '{{ site.baseurl }}' + feature.image;
      if (featureTitle) featureTitle.textContent = feature.title;
      if (featureCategory) featureCategory.textContent = feature.category;
      if (featureDescription) featureDescription.textContent = feature.description;
      setLinks(featureLinks, feature.url);
    }
  }
})();
</script>
