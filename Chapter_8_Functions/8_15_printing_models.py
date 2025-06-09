### 8-15. Printing Models:

import printing_functions

requested_models = ["chuck_jug", "proteza", "bow_tie"]
completed_models = []

printing_functions.start_3d_print(requested_models, completed_models)
printing_functions.print_completed(completed_models)