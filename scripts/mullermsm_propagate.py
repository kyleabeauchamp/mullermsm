#!/usr/bin/env python
import os, sys
import argparse
import mullermsm
from mullermsm import metric
from mullermsm import muller
import mdtraj as md
import mdtraj.io
import numpy as np
import IPython as ip
import random
import cPickle as pickle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--n_trajs', help='number of trajectories. Default=10', type=int, default=10)
    parser.add_argument('-t', '--traj_length', help='trajectories length. Default=10000', type=int, default=10000)
    args = parser.parse_args()
    
    # these could be configured
    kT = 35.0
    dt = 0.1
    mGamma = 1000.0
    
    forcecalculator = muller.muller_force()
        
    for i in range(args.n_trajs):
        print 'simulating traj %s' % i
        
        # select initial configs randomly from a 2D box
        initial_x = [random.uniform(-1.5, 1.2), random.uniform(-0.2, 2)]
        print 'starting conformation from randomly sampled points (%s, %s)' % (initial_x[0], initial_x[1])
        print 'propagating for %s steps on the Muller potential with a Langevin integrator...' % args.traj_length
        
        positions = muller.propagate(args.traj_length, initial_x, kT, dt, mGamma, forcecalculator)
        md.io.saveh("./positions.h5", positions)
    
if __name__ == '__main__':
    main()
