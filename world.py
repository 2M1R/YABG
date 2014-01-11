from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.bullet import BulletWorld, BulletPlaneShape, BulletRigidBodyNode
from panda3d.core import Vec3

class World:
    def world_create(self, sizex, sizey):
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))

        # Load model
        self.ground = Showbase.loader.loadModel("Models/floor_basic.egg")

        # Reparent
        self.ground.reparentTo(ShowBase.render)

        # Scale and position model
        self.ground.setScale(sizex, sizey, 0)
        self.ground.setPos(0, 0, 0)

        self.shape = BulletPlaneShape(Vec3(0, 0, 1), 1)

        self.node = BulletRigidBodyNode('Floor')
        self.node.addShape(self.shape)

        self.np = render.attachNewNode(self.node)
        self.np.setScale(sizex, sizey, 0)
        np.setPos(0, 0, 0)

        self.world.attachRigidBody(self.node)

        ShowBase.taskMgr.add(update, 'update')

    def update(self, task):
        dt = ShowBase.globalClock.getDt()
        self.world.doPhysics(dt, 10, 1.0/180.0)
        return Task.cont