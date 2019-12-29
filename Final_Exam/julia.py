from PIL import Image

# Image Configuration
w, h = 800, 800
bitmap = Image.new("RGB", (w, h), "white")
image = bitmap.load()


c = complex(-1.5, 0.2)
N = 200


for x in range(w):
    for y in range(h):
        # map from pixels coordinates to [-1.5,1.5]
        z = complex(3*(x - w/2)/w, 3*(y - h/2)/h)

        color = (255, 255, 255)
        lucky = False
        if(abs(z) == 0):
            lucky = True
        # Orbit
        for iteration in range(N):
            if(lucky): print(z)
            z = z**2 + c
            if(abs(z)) > max(abs(c), 2):
                color = (0, 0, 0)
                break

        image[x, y] = color


bitmap.show()
