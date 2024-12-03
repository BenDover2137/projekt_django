Struktura strony
1. Strona główna:
Lista zgłoszonych problemów:
Dla użytkowników: widoczne tylko ich zgłoszenia.
Dla administratorów: widoczne wszystkie zgłoszenia.
Informacje dla każdego zgłoszenia:
Tytuł.
Status (np. otwarte, w trakcie rozwiązywania, zamknięte).
Data zgłoszenia.
Przyciski:
"Zgłoś problem" (formularz do zgłaszania nowego problemu).
"Zobacz szczegóły" (przenosi do widoku szczegółowego zgłoszenia).
2. Widok zgłaszania nowego problemu:
Formularz umożliwiający użytkownikowi podanie:
Tytułu problemu.
Opisu problemu.
Automatyczne przypisanie:
Statusu (domyślnie otwarte).
Daty zgłoszenia.
Przycisk "Wyślij zgłoszenie".
3. Widok szczegółowy zgłoszenia:
Wyświetlenie:
Tytułu.
Opisu problemu.
Statusu.
Odpowiedzi od administratora (jeśli zostały dodane).
Daty zgłoszenia i ostatniej aktualizacji.
Użytkownik:
Widzi odpowiedzi, ale nie może edytować zgłoszenia.
Administrator:
Może dodawać odpowiedzi do zgłoszenia.
Może zmieniać status zgłoszenia (np. na w trakcie rozwiązywania lub zamknięte)
4. Panel administracyjny:
Dostępny tylko dla administratorów (wbudowany Django Admin).
Zarządzanie zgłoszeniami i użytkownikami.
Modele
1. Model Ticket (Zgłoszenie):
Pola:
title (tytuł zgłoszenia).
description (opis problemu).
status (status zgłoszenia, np. otwarte, w trakcie, zamknięte).
created_at (data utworzenia, automatyczna).
updated_at (data ostatniej aktualizacji).
author (powiązanie z modelem użytkownika Django).
2. Model Response (Odpowiedź):
Pola:
ticket (powiązanie z modelem Ticket).
content (treść odpowiedzi).
created_at (data dodania odpowiedzi).
author (powiązanie z użytkownikiem – administrator)
3. Model Użytkownika (wbudowany Django):
Role użytkowników:
Użytkownik (domyślnie).
Administrator (przydzielony w Django Admin).
Funkcjonalności
1. Dla użytkowników:
Zgłaszanie problemów za pomocą formularza.
Przeglądanie swoich zgłoszeń.
Oglądanie odpowiedzi administratorów.
2. Dla administratorów:
Przeglądanie wszystkich zgłoszeń.
Odpowiadanie na zgłoszenia.
Zmiana statusu zgłoszeń.
3. Wspólne:
Widok szczegółowy zgłoszeń.
Automatyczne sortowanie zgłoszeń według statusu (np. otwarte jako pierwsze).
