#include <iostream>
#include <random>

#include "image.hpp"
#include "perlin.hpp"

int main() {
	std::cout << "Hello, User!" << std::endl;
	
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_real_distribution<> dis(1.0, 2147483648.0);
	float number = dis(gen);

	perlin::Perlin map((long)number);

	Image image;
	image.generate(512, 512);

	double frequency = 16;
	double fx = image.getWidth() / frequency;
	double fy = image.getHeight() / frequency;

	for (int y = 0; y < 512; y++) {
		for (int x = 0; x < 512; x++) {
			double p = map.accumulatedNoise2D(x / fx, y / fy, 8, 2.0f, 0.25f);
			image.setPixel(x, y, p, p, p);
		}
	}

	image.write("out.bmp");

	return 0;
}
