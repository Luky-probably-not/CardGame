package main

import (
	"fmt"
)
type Card struct {
	name string
	effect string
	stat int
}

type Enemy struct {
	name string
	atk int
	hpmax int
	currentHp int
	action string
	listActions []string
}

type Player struct {
	hpmax int
	currentHp int
	deck []Card
	mana int
}


func main() {
	karte := Card{
		name: "frappe",
		effect: "atk",
		stat: 3,
	}
	joueur := Player{
		hpmax: 20,
		currentHp: 20,
		deck: []Card{karte},
		mana: 3,
	}
	zombie := Enemy{
		name: "Zombie",
		atk: 3,
		hpmax: 15,
		currentHp: 15,
		action: "atk",
		listActions: []string{"atk","def","buff"},
	}
	Display(karte,joueur,zombie)
}

