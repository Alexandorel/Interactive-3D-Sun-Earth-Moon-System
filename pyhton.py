from vpython import canvas, sphere, vector, color, rate, cos, sin, local_light, textures

# Scene setup
scene = canvas(title="Sun-Earth-Moon System (Camera Fixed on Sun)",
               width=800, height=600,
               center=vector(0, 0, 0), 
               background=color.black,
               userzoom=True,
               userspin=True)

scene.lights = []

# Celestial objects
sun = sphere(pos=vector(0, 0, 0), radius=2.0, color=vector(1, 0.35, 0), emissive=True)
scene.center = sun.pos
sun_light = local_light(pos=vector(0, 0, 0), color=color.white)

earth = sphere(pos=vector(7, 0, 0), radius=0.8, texture=textures.earth)
moon = sphere(pos=vector(8.5, 0, 0), radius=0.22, texture=textures.rough, color=color.gray(0.8))

rotation_axis = vector(0, 1, 0)

# Movement parameters
earth_orbit_speed = 0.015
moon_orbit_speed = 0.06
earth_angle = 0
moon_angle = 0
moon_earth_distance = 1.4

sun_spin_speed = 0.002
earth_spin_speed = 0.05  
moon_spin_speed = 0.01

print("3D Scene started successfully!")

# Animation loop
while True:
    rate(60)
    
    # Axial rotation (Spinning)
    sun.rotate(angle=sun_spin_speed, axis=rotation_axis)
    earth.rotate(angle=earth_spin_speed, axis=rotation_axis)
    moon.rotate(angle=moon_spin_speed, axis=rotation_axis)
    
    # Orbital revolution
    earth_angle += earth_orbit_speed
    earth.pos.x = 7 * cos(earth_angle)
    earth.pos.z = 7 * sin(earth_angle)
    
    moon_angle += moon_orbit_speed
    moon.pos.x = earth.pos.x + moon_earth_distance * cos(moon_angle)
    moon.pos.z = earth.pos.z + moon_earth_distance * sin(moon_angle)