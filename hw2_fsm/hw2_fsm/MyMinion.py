'''
 * Copyright (c) 2014, 2015 Entertainment Intelligence Lab, Georgia Institute of Technology.
 * Originally developed by Mark Riedl.
 * Last edited by Mark Riedl 05/2015
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import sys, pygame, math, numpy, random, time, copy
from pygame.locals import * 

from constants import *
from utils import *
from core import *
from moba import *

class MyMinion(Minion):
	
	def __init__(self, position, orientation, world, image = NPC, speed = SPEED, viewangle = 360, hitpoints = HITPOINTS, firerate = FIRERATE, bulletclass = SmallBullet):
		Minion.__init__(self, position, orientation, world, image, speed, viewangle, hitpoints, firerate, bulletclass)
		self.states = [Idle]
		### Add your states to self.states (but don't remove Idle)
		### YOUR CODE GOES BELOW HERE ###
		self.states.append(Move)
		self.states.append(AttackTarget)
		self.states.append(Wait)
		### YOUR CODE GOES ABOVE HERE ###

	def start(self):
		Minion.start(self)
		self.changeState(Idle)





############################
### Idle
###
### This is the default state of MyMinion. The main purpose of the Idle state is to figure out what state to change to and do that immediately.

class Idle(State):
	
	def enter(self, oldstate):
		State.enter(self, oldstate)
		# stop moving
		self.agent.stopMoving()
	
	def execute(self, delta = 0):
		State.execute(self, delta)
		### YOUR CODE GOES BELOW HERE ###
		if len(self.agent.world.getEnemyBases(self.agent.team)) !=0 \
			or len(self.agent.world.getEnemyTowers(self.agent.team)) !=0:
			self.agent.changeState(Move)

		### YOUR CODE GOES ABOVE HERE ###
		return None

##############################
### Taunt
###
### This is a state given as an example of how to pass arbitrary parameters into a State.
### To taunt someome, Agent.changeState(Taunt, enemyagent)

class Taunt(State):

	def parseArgs(self, args):
		self.victim = args[0]

	def execute(self, delta = 0):
		if self.victim is not None:
			print("Hey " + str(self.victim) + ", I don't like you!")
		self.agent.changeState(Idle)

##############################
### YOUR STATES GO HERE:
class Move(State):
	def enter(self, oldState):
		if self.agent.world.getEnemyTowers(self.agent.team):
			self.agent.navigateTo(self.agent.world.getEnemyTowers(self.agent.team)[0].position)
		elif self.agent.world.getEnemyBases(self.agent.team):
			self.agent.navigateTo(self.agent.world.getEnemyBases(self.agent.team)[0].position)
		else:
			self.agent.changeState(Idle)
	def execute(self, delta = 0):

		if self.agent.world.getEnemyTowers(self.agent.team):
			attack = self.agent.world.getEnemyTowers(self.agent.team)[0]
		elif self.agent.world.getEnemyBases(self.agent.team):
			attack = self.agent.world.getEnemyBases(self.agent.team)[0]
		else:
			self.agent.changeState(Idle)
		if self.agent.getState() != Idle:
			if not self.agent.isMoving():
				if self.agent.world.getEnemyTowers(self.agent.team):
					self.agent.navigateTo(attack.position)
				elif self.agent.world.getEnemyBases(self.agent.team):
					self.agent.navigateTo(attack.position)

			for enemy in self.agent.world.getEnemyNPCs(self.agent.team):
				if enemy in self.agent.getVisible() and distance(self.agent.position, enemy.position) < 200 and distance(self.agent.position, attack.position) > 250:
					self.agent.turnToFace(enemy.position)
					self.agent.shoot()
					break

			if self.agent.world.getEnemyTowers(self.agent.team):
				for tower in self.agent.world.getEnemyTowers(self.agent.team):
					if tower in self.agent.getVisible() and distance(self.agent.position, tower.position) < 200:
						self.agent.changeState(AttackTarget, tower)
			else:
				base = self.agent.world.getEnemyBases(self.agent.team)[0]
				if base in self.agent.getVisible() and distance(self.agent.position, base.position) < 200:
					self.agent.changeState(AttackTarget, base)
			for teammate in self.agent.world.getNPCsForTeam(self.agent.team):
				if teammate != self.agent and distance(self.agent.position, teammate.position) < 30 and teammate.isMoving():
					self.agent.changeState(Wait, self)

'''

'''






class AttackTarget(State):
	def parseArgs(self, args):
		self.attack = args[0]
	def enter(self, oldstate):
		self.agent.turnToFace(self.attack.position)
		#self.agent.stopMoving()
	def execute(self,delta = 0):
		self.agent.turnToFace(self.attack.position)
		self.agent.shoot()
		if distance(self.agent.position, self.attack.position) < 20:
			self.agent.stopMoving()
		if self.attack.getHitpoints() == 0:
			self.agent.changeState(Move)


class Wait(State):
	def enter(self, oldState):
		self.agent.stopMoving()
	def execute(self,delta = 0):
		stopWaiting = False
		for teammate in self.agent.world.getNPCsForTeam(self.agent.team):
			if teammate != self.agent and distance(self.agent.position, teammate.position) < 30 and teammate.isMoving():
				self.agent.stopMoving()
				stopWaiting = False
				break
			else:
				stopWaiting = True
		if stopWaiting == True:
			self.agent.changeState(Move)





