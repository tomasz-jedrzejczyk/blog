---
title: ai daily usage
date: 2026-10-15
---

Na projekcie w pracy podjąłem się wyzwania rozpoczęcia testów automatycznych do testowania backendu. Głównym zadaniem będzie zautomatyzować scenariusze z historyjek użytkowników z poziomu API. 

Miałem wolną rękę odnośnie wyglądu i używanych bibliotek. Jedynie musiałem zwracać uwage na ilość przepalanych tokenów. Z tego względu na zadania wymagające większego zaangażowania używałem mocniejszych modeli a na resztę ‘AUTO’.

Początki były na raczej oczywiste. Przełączenie czatu na planowanie i sprecyzowanie jak ma wyglądać ogół projektu, jakie ma być rozłożenie zasobów, folderów. Założenia bardzo mi się podobały i wszystko zaakceptowałem. Pierwsze klasy, metody i funkcje wyglądały naprawde dobrze dlatego zgadzałem się na każdą zmiane. Starałem się często aktualizować plik README.md aby kolejne iteracje wiedziały jak ma wyglądać architektura projektu.  

Problemy zaczęły się dość szybko kiedy potrzebowałem zrobić refaktor. Chciałem, żeby jedna z metoda była wyniesiona do innej klasy i przyjmowała parametr i propozycją od inteligencji był interfejs. Wydało mi się trochę jak przestrzał ale zaufałem. No i żałowałem. Strasznie przekombinował mi dość prostą funkcjonalność. Kolejne rozbudowania automatyzacji nie ułatwiały czytelność a jedynie jeszcze więcej linii kodu i dodatkowe klasy. Nowo dodane funkcjonalności duplikowały już istniejące nie biorąc ich pod uwagę stare. 

W momencie kiedy miałem interfejs który był rozszerzany o inną klasę a struktura folderów tylko się powiększała, powiedziałem dość. Usunąłem wszystkie dodatkowe klasy do momentu kiedy miałem podstawowy kod. Potrzebowałem na to naprawde dużo czasu, ale chciałem dojść do momentu kiedy rozumiem kod, nie jest on przekombinowany a logiczny i czytelny.

Lekcja którą wyciągnąłem to nie dawanie mu zbyt dużego zadania. Polecenia powinny być niewielkie i dobrze opisane. Dodanie całej nowej metody która ma robić request do bazy jest zbyt ogólna. Najlepiej stworzyć metodę potem opisać że potrzebujemy w tej metodzie request HTTP GET do takiego endpointa który ma takie header i takie body.

Moje problemy wynikały tylko i wyłącznie z moich niedopatrzeń. Powinno się szybciej reagować na niepokojące zachowania modelu. Ograniczać wprowadzane zmiany do jak największego minimum i oceniać prace jak najczęściej. 

Nie sądze, żeby AI przyspieszyło moje pisanie kodu ale chyba dlatego, że jeszcze uczę się z niego korzystać. Jak z każdym narzędziem potrzeba czasu, żeby go zrozumieć.

Tekst w całości był napisany przeze mnie. 

