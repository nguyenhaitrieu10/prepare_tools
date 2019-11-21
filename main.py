from google_sheet import read_google_sheet
from topology import topological_sort, preprocess_data
from file_process import generate_deploy_files
from graph import draw_graph

if __name__ == '__main__':
    # read data from google sheet
    list_of_records = read_google_sheet(secret_key_file='input_files/secret.json')
    print(list_of_records)

    # parse data
    apps = preprocess_data(list_of_records)
    print(apps)

    # topology sort
    result, jobs_order = topological_sort(apps)
    print(jobs_order)

    if result == 'OK':
        generate_deploy_files(jobs_order)
        draw_graph(apps)




