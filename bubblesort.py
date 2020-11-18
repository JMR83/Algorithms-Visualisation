from manimlib.imports import *



class BubbleSortScene(Scene):

	CONFIG = {"camera_config" : {"background_color" : "#000000 " } }
	
	arr = [12, 8, 9, 2, 4, 18, 1]
	ANIMATION_TIME = 0.5


	def highlightNeighboringNumbers(self, nums, j, scale = 2.0, color = RED):
		self.play(
			nums[j].scale, scale,
			nums[j].set_color, color,
			nums[j+1].scale, scale,
			nums[j+1].set_color, color,
			run_time = self.ANIMATION_TIME
		)
		self.wait()



	def construct(self):

		title = TextMobject("Bubble Sort", color = GOLD).scale(2)
		title.to_corner(UL)

		self.play(
			ShowCreation(title)
		)
		self.wait()

		N = len(self.arr)
		list_of_squares = [Square().scale(0.6) for i in self.arr]

		# unpack squares and add it to VGroup
		squares = VGroup(*list_of_squares)

		squares.arrange(buff = 0.)
	
	
		nums = [TextMobject(str(i)) for i in self.arr]
		for i in range(N):
			nums[i].move_to(squares[i].get_center())

		self.add(squares, *nums)
		self.wait(2)

		for i in range(N):
			for j in range(N-i-1):

				self.highlightNeighboringNumbers(nums,j)


				if self.arr[j] > self.arr[j+1]:

					self.play(
						Swap(nums[j], nums[j+1])
					)

				

					# swap numbers
					self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

					# swap TextMobjects
					nums[j], nums[j+1] = nums[j+1], nums[j]

				# back transformation
				self.highlightNeighboringNumbers(nums,j, scale = 0.5, color = WHITE)

		self.wait(5)


		
		
		
					
			

			

			







	'''

		for i in range(N-1):

			k1 = self.indexTransform(i)
			k2 = self.indexTransform(i+1)

			unscaled1 = list_of_numbers[k1].copy()
			unscaled2 = list_of_numbers[k2].copy()

			self.play(
				ReplacementTransform(list_of_numbers[k1], unscaled1),
				ReplacementTransform(list_of_numbers[k2], unscaled2)
			)

			



			scaled1 = TextMobject(self.list_as_string[i], color = RED).scale(3.)
			scaled1.move_to(unscaled1)

			scaled2 = TextMobject(self.list_as_string[i+1], color = RED).scale(3.)
			scaled2.move_to(unscaled2)



			self.play(
				ReplacementTransform(unscaled1, scaled1), 
				ReplacementTransform(unscaled2, scaled2),
				run_time = 2
			)

			if(self.list_as_ints[i] > self.list_as_ints[i+1]):

				self.swap_visual(scaled1, scaled2)

				self.swap(self.list_as_string, i , i+1)
				self.swap(self.list_as_ints, i, i+1)

				unscaled1, unscaled2 = self.back_transform(self.list_as_string, i, i+1, scaled1, scaled2)

				self.play(
					ReplacementTransform(scaled2, unscaled1),
					ReplacementTransform(scaled1, unscaled2),
					run_time = 2.
				)

			else:
				unscaled1, unscaled2 = self.back_transform(self.list_as_string, i+1, i, scaled1, scaled2)

				self.play(
					ReplacementTransform(scaled2, unscaled1),
					ReplacementTransform(scaled1, unscaled2),
					run_time = 2.
				)











		self.wait(5)

	'''