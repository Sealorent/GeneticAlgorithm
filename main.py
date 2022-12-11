from flask import Flask, request, jsonify
app = Flask(__name__)
import pygad
import numpy




@app.route('/prob/', methods=['GET'])
def respond():
    
    

    # Retrieve the name from the url parameter /getmsg/?name=
    cr = request.args.get("cr", None)
    mr = request.args.get("mr", None)
    generation = request.args.get("gen",None)

    # For debugging
   

    # Check if the user sent a name at all
    if not cr and mr and gen:
        response["ERROR"] = "No name found. Please send a full."
 
    else:
        
        function_inputs = [400,600,800,10,15,31,50,70,100,40,60,100]
        
        desired_output = 12

        def fitness_func(solution, solution_idx):
            output = numpy.sum(numpy.array(function_inputs)) - numpy.sum(numpy.array(solution)) 
            desire = pow(desired_output,2)
            fitness = 1.0 / (output / desire  + 1)
            return fitness


        fitness_function = fitness_func

        num_generations = 100
        num_parents_mating = 3

        sol_per_pop = 8
        num_genes = len(function_inputs)
            
        init_range_low = 0
        init_range_high = 800

        crossover_prob=float(cr)
        mutation_prob=float(mr)


        parent_selection_type = "sss"
        keep_parents = 3

        crossover_type = "two_points"

        mutation_type = "random"
        mutation_percent_genes = 10


        ga_instance = pygad.GA(num_generations=num_generations,
                            num_parents_mating=num_parents_mating,
                            fitness_func=fitness_function,
                            sol_per_pop=sol_per_pop,
                            num_genes=num_genes,
                            crossover_probability=crossover_prob,
                            mutation_probability=mutation_prob,
                            init_range_low=init_range_low,
                            init_range_high=init_range_high,
                            parent_selection_type=parent_selection_type,
                            gene_space=[range(0, 400), range(400, 600), range(400, 800), range(0, 10), range(5, 15), range(10, 31), range(0, 50), range(0, 70),range(0, 100), range(0,40),range(0, 60),range(0, 100)],
                            keep_parents=keep_parents,
                            crossover_type=crossover_type,
                            mutation_type=mutation_type,
                            mutation_percent_genes=mutation_percent_genes)


        ga_instance.run()

        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        # print("Parameters of the best solution : {solution}".format(solution=solution))
        # print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
        # print(solution=solution)

        prediction = numpy.sum(numpy.array(solution))
        # print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))
        # print(pygad.__version__)
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
        
        result = [solution.tolist(), solution_fitness]

    # Return the response in json format
    return jsonify(result)



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)