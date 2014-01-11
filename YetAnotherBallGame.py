from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.bullet import BulletWorld, BulletPlaneShape, BulletRigidBodyNode
from panda3d.core import Vec3

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #self.world = BulletWorld()
        #self.world.setGravity(Vec3(0, 0, -9.81))

        #self.taskMgr.add(self.update, 'update')

        #self.shape = BulletPlaneShape(Vec3(0, 0, 1), 1)

        #self.node = BulletRigidBodyNode('Floor')
        #self.node.addShape(self.shape)

        # Load model
        self.ground = self.loader.loadModel("Models/floor_basic.egg")

        # Reparent
        self.ground.reparentTo(self.render)

        # Apply scale and position transforms on the model.
        self.ground.setScale(100, 100, 0)
        self.ground.setPos(0, -1, 0)

        #self.np = self.render.attachNewNode(self.node)
        #self.np.setPos(0, 0, -2)

        #self.world.attachRigidBody(self.node)

    def update(self, task):
        dt = globalClock.getDt()
        self.world.doPhysics(dt, 10, 1.0/180.0)
        return Task.cont

app = Game()
app.run()