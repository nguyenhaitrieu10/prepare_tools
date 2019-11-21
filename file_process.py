
def generate_deploy_files(jobs_order):
    f = open("output_files/moltres.yml", "w")
    g = open("output_files/deploy_list.txt", "w")

    for job in jobs_order:
        f.write('    - name: %s\n' % job['id'])
        f.write('      inCharge: %s\n' % job['inCharge'])
        g.write('vn.live.k8s/%s\n' % job['id'])
