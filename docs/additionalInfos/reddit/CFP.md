## Overview

1. Requester(s): Eric Volz [GitHub](https://github.com/eric-volz)
2. Amount requested in DFI: 1800
3. Receiving address: df1qdx0mllcvvrdfcrstyvp2pu4szp2pct5njcgwev
4. [Reddit discussion thread](https://www.reddit.com/r/defiblockchain/comments/tdhbj6/cfp_defichain_python_library_1800_dfi/)
5. Proposal fee (10 DFI) txid: 0a454f39213285395e7420b1680378f46516b5389d7b4c42830795adb4487cd7

## Describe the purpose The Problem

The Python Library offers every Python programmer an easy entry into the Defichain ecosystem!

This allows a quick and easy development of new applications or even a more straightforward creation of trading bots.

Through a via "pip" downloadable package it is possible to call any CLI command through a Python function and to work with the output of the function directly in Python.

This Python library has the same functionality as the Jellyfish Full Node RPC library.

Furthermore, all commands of the Ocean REST API are mapped by functions.

### Example calls:

#### Import and connection:

```
from defichain import Node # import

node = Node(connection, port, user, password) # connection to the Node
```

##### Getblockcount:

```
blockcount = node.blockchain.getblockcount() # Query to node

print(blockcount) # blockcount
```

##### Compositswap:

```
txid = node.poolpair.compositeswap(address, "BTC", 1 address, "USDC", 40000) # Compositswap from BTC to USDC

print(txid) # Txid of the swap
```

##### Ocean Rest API:

```
from defichain import Ocean # import

price = Ocean.prices.get("DFI", "USD") # call

print(price) # current DFI price
```

#### Precondition:

For everything except the Ocean Rest API commands a Defichain Full Node is required!

## How will the fund be spent?

### Development costs:

\--> About 250 individual CLI commands

\--> 30 min per command with implementation, testing and documentation, publication

\--> Hourly rate: $50

\--> DFI Price: \~$3.45

\--> 250 commands \* 30 min = 7500 min = 125h --> 125h \* $50 = $6250 (25% taxes in Germany)

\--> $6250 / $3.45 \~= 1800 DFI

## What comes in the future

* Adding new commands
* Neat, understandable and simple documentation
* Algorithm for analyzing the blockchain
  * Stores blocks and transactions in a database
  * Can calculate any state of a liquidity pool on a given block based on this data

## How does this CFP benefit the DeFiChain community?

Python is one of the most widely used programming languages in the world, so this is an easy entry point for Python development on Defichain.

This library allows the developers of new applications to fully concentrate on them. The library takes care of driving the node that is in the background.

This accelerates the development time of future applications.

In addition, this library provides further decentralization, because a large part of the Defichain ecosystem has so far been based on the Ocean API and the JavaScript (Typescript) programming language.

---

## Überblick

1. Anforderer: Eric Volz [GitHub](https://github.com/eric-volz)
2. Angefragte Menge in DFI: 1800
3. Empfangsadresse: df1qdx0mllcvvrdfcrstyvp2pu4szp2pct5njcgwev
4. [Reddit Diskussionsthread](https://www.reddit.com/r/defiblockchain/comments/tdhbj6/cfp_defichain_python_library_1800_dfi/)
5. Vorschlagsgebühr (10 DFI) txid: 0a454f39213285395e7420b1680378f46516b5389d7b4c42830795adb4487cd7

## Beschreibe den Zweck

Die Python Library bietet jedem Python Programmierer einen einfachen Einstieg in das Defichain Ökosystem!

Hierdurch wird eine schnelle und einfache Entwicklung von neuen Anwendungen oder auch ein unkomplizierteres Erstellen von Trading Bots ermöglicht.

Durch ein via "pip" herunterladbares Package wird es möglich, jeden CLI Command durch eine Python Funktion aufzurufen und mit dem Output der Funktion, direkt in Python weiter zu arbeiten.

Diese Python Library besitzt die selbe Funktionalität wie die Jellyfish Full Node RPC Library.

Des weitern werden alle Commands der Ocean REST API durch Funktionen abgebildet.

### Beispielaufrufe:

#### Import und Verbindungsaufbau:

```
from defichain import Node # Import

node = Node(verbindung, port, benutzer, passwort) # Verbindungsaufbau zum Node
```

##### Getblockcount:

```
blockcount = node.blockchain.getblockcount() # Abfrage ans Node

print(blockcount) # Blockcount
```

##### Compositswap:

```
txid = node.poolpair.compositeswap(address, "BTC", 1 address, "USDC", 40000) # Compositswap von BTC zu USDC

print(txid) # Txid des Swaps
```

##### Ocean Rest API:

```
from defichain import Ocean # Import

price = Ocean.prices.get("DFI", "USD") # Aufrufe

print(price) # Preis von DFI
```

#### Voraussetzung:

Für alles außer die Ocean Rest API Befehle ist ein Defichain Full Node notwendig!

## Wie wird das Geld ausgegeben?

### Entwicklungskosten:

\--> Circa 250 individuelle CLI Befehle

\--> 30 min pro Befehl mit Implementation, Testen und Dokumentation, Veröffentlichung

\--> Stundensatz: 50$

\--> DFI Preis: \~3.45$

\--> 250 Befehle \* 30 min = 7500 min = 125h --> 125h \* 50$ = 6250$ (25% Steuern in Deutschland)

\--> 6250$ / 3.45$ \~= 1800 DFI

## Was kommt in der Zukunft

* Hinzufügen neuer Commands
* Ordentliche, verständliche und einfache Dokumentation
* Algorithmus zum Analysieren der Blockchain
  * Speichert Blocks und Transactions in einer Datenbank
  * Kann auf Grundlage dieser Daten jeden Stand eines Liquidity Pools zu einem bestimmten Block berechnen

## Wie kommt diese CFP der DeFiChain-Community zugute?

Python ist eine der meist verwendeten Programmiersprachen der Welt, weshalb dies ein einfacher Einstiegspunkt für die Python Entwicklung auf der Defichain ist.

Diese Library ermöglicht es den Entwicklern von neuen Anwendungen sich voll und ganz auf diese zu konzentrieren. Durch die Library wird das Ansteuern, des im Hintergrund befindlichen Nodes übernommen.

Dies beschleunigt die Entwicklungszeit zukünftiger Anwendungen.

Zudem ist durch diese Library eine weitere Dezentralisierung gegeben, denn ein Großteil des Defichain Ökosystems basiert bisher auf der Grundlage von Ocean API und der Programmiersprache JavaScript (Typescript).