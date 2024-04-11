import os
import re

cask_path = "../cask_cropped.ttl"

# read T-Box
with open(cask_path, 'r', encoding='utf-8') as cask_file:
	cask_content = cask_file.read()
    
	folder = '../metaprompts'

	# open zero-shot and replace tasks
	zero_shot_meta_path = os.path.join(folder, "0_zero-shot.txt")
	with open(zero_shot_meta_path, 'r', encoding='utf-8') as file:
		zero_shot_meta_content = file.read()
		
		# Replace T-Box
		zero_shot_meta_content_with_t_box = re.sub(re.escape("${T-Box}"), cask_content, zero_shot_meta_content)

		task_description_folder = "../task-descriptions"
		
		for task_description_file_name in os.listdir(task_description_folder):
			task_description_path = os.path.join(task_description_folder, task_description_file_name)
			
			with open(task_description_path, 'r', encoding='utf-8') as task_description_file:
				task_description_content = task_description_file.read()
                        
				# Replace task
				prompt = re.sub(re.escape("${Task}"), task_description_content, zero_shot_meta_content_with_t_box)
                        
				# Store file
				prompt_folder_path = "./0_zero-shot-prompts/0_" + task_description_file_name
				with open(prompt_folder_path, 'w', encoding='utf-8') as file:
					file.write(prompt)


	# open one-shot and replace tasks
	one_shot_meta_path = os.path.join(folder, "1_one-shot.txt")
	with open(one_shot_meta_path, 'r', encoding='utf-8') as file:
		one_shot_meta_content = file.read()
		
		# Replace T-Box
		one_shot_meta_content_with_t_box = re.sub(re.escape("${T-Box}"), cask_content, one_shot_meta_content)

		# Read all task descriptions
		task_description_folder = "../task-descriptions"
		for task_description_file_name in os.listdir(task_description_folder):
			task_description_path = os.path.join(task_description_folder, task_description_file_name)
			
			with open(task_description_path, 'r', encoding='utf-8') as task_description_file:
				task_description_content = task_description_file.read()
                        
				# Replace task
				prompt = re.sub(re.escape("${Task}"), task_description_content, one_shot_meta_content_with_t_box)

				# Replace example task and capability 1
				with open("../examples/coffeemaking-task.txt", 'r', encoding='utf-8') as coffe_task_description_file:
					coffee_task_description_content = coffe_task_description_file.read()
					prompt = re.sub(re.escape("${Example Task}"), coffee_task_description_content, prompt)

				with open("../examples/coffeemaking.ttl", 'r', encoding='utf-8') as coffe_cap_file:
					coffe_cap_file_content = coffe_cap_file.read()
					prompt = re.sub(re.escape("${Example Capability A-Box}"), coffe_cap_file_content, prompt)
                        
				# Store file
				prompt_folder_path = "./1_one-shot-prompts/1_" + task_description_file_name
				with open(prompt_folder_path, 'w', encoding='utf-8') as file:
					file.write(prompt)


	# open few-shot and replace tasks
	few_shot_meta_path = os.path.join(folder, "2_few-shot.txt")
	with open(few_shot_meta_path, 'r', encoding='utf-8') as file:
		few_shot_meta_content = file.read()
		
		# Replace T-Box
		few_shot_meta_content_with_t_box = re.sub(re.escape("${T-Box}"), cask_content, few_shot_meta_content)

		# Read all task descriptions 
		task_description_folder = "../task-descriptions"
		for task_description_file_name in os.listdir(task_description_folder):
			task_description_path = os.path.join(task_description_folder, task_description_file_name)
			
			with open(task_description_path, 'r', encoding='utf-8') as task_description_file:
				task_description_content = task_description_file.read()

				# Replace task
				prompt = re.sub(re.escape("${Task}"), task_description_content, few_shot_meta_content_with_t_box)

				# Replace example task and capability 1
				with open("../examples/coffeemaking-task.txt", 'r', encoding='utf-8') as coffe_task_description_file:
					coffee_task_description_content = coffe_task_description_file.read()
					prompt = re.sub(re.escape("${Example Task 1}"), coffee_task_description_content, prompt)

				with open("../examples/coffeemaking.ttl", 'r', encoding='utf-8') as coffe_cap_file:
					coffe_cap_file_content = coffe_cap_file.read()
					prompt = re.sub(re.escape("${Example Capability A-Box 1}"), coffe_cap_file_content, prompt)


				# Replace example task and capability2
				with open("../examples/multiplication-task.txt", 'r', encoding='utf-8') as multiplication_task_description_file:
					multiplication_task_description_content = multiplication_task_description_file.read()
					prompt = re.sub(re.escape("${Example Task 2}"), multiplication_task_description_content, prompt)

				with open("../examples/multiplication.ttl", 'r', encoding='utf-8') as multiplication_cap_file:
					multiplication_cap_file_content = multiplication_cap_file.read()
					prompt = re.sub(re.escape("${Example Capability A-Box 2}"), multiplication_cap_file_content, prompt)


				# Replace example task and capability 3
				with open("../examples/distillation-task.txt", 'r', encoding='utf-8') as distillation_task_description_file:
					distillation_task_description_content = distillation_task_description_file.read()
					prompt = re.sub(re.escape("${Example Task 3}"), distillation_task_description_content, prompt)

				with open("../examples/distillation.ttl", 'r', encoding='utf-8') as distillation_cap_file:
					distillation_cap_file_content = distillation_cap_file.read()
					prompt = re.sub(re.escape("${Example Capability A-Box 3}"), distillation_cap_file_content, prompt)
                
				# Store file
				prompt_folder_path = "./2_few-shot-prompts/2_" + task_description_file_name
				with open(prompt_folder_path, 'w', encoding='utf-8') as file:
					file.write(prompt)

print("Alle Dateien wurden bearbeitet.")