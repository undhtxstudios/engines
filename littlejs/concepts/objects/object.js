// LittleJS can be used as an object oriented system by extending 
// the base class EngineObject with your own. This lightweight class 
// provides many useful features including physics, collision, 
// parent/child system, and sorted rendering. These objects are 
// added to the global list of objects where they will automatically 
// be updated and rendered until destroyed.

class MyObject extends EngineObject 
{
    constructor(pos, size, tileInfo, angle)
    {
        super(pos, size, tileInfo, angle);
        // setup object
    }

    update()
    {
        // update object physics and position
        super.update(); 
    }

    render()
    {
        // draw object as a sprite
        super.render();
    }
}