/**
 * ConvexHull.java
 * 
 * Helen Hu and Greg Gagne
 * 
 * September 2016
 */

import java.util.*;
import java.awt.Point;
import java.awt.Polygon;

public class ConvexHull {
	// all the points in the collection
	private ArrayList<Point> points;
	
	// the polygon that makes up the convex hull
	private Polygon hull;
	
	// a boolean to check if the convex hull needs to be recalculated
	private boolean hullCalculated = true;
	
	// constructor
	public ConvexHull() {
		points = new ArrayList<Point>();
		hull = new Polygon();
	}

	/**
	 * Adds a single point to the collection
	 * @param point
	 */
	public void addPoint(Point point) {
		this.points.add(point);
		hullCalculated = false;
	}		

	/** returns a specific point from the collection
	 * 
	 * @param i: a number between 0 and the number of points
	 * @return the Point indexed
	 */
	public Point getPoint(int i){
		if (0 <= i && i < points.size())
			return points.get(i);
		else
			throw new NoSuchElementException();
	}
	
	/** 
	 * 
	 * @return an ArrayList with all the Points in the collection 
	 */
	public ArrayList<Point> getPoints() {
		return points;
	}
	
	/**
	 * removes all the points from the collection
	 */
	public void clear() {
		points.clear();
		hull.reset();
		hullCalculated = true;
	}

	/** returns the number of points in the current collection */
	public int getNumber() {
		return points.size();
	}
	
	/** returns the convex hull for the current set of points */
	public Polygon getHull() {
		if (!hullCalculated)
			calculateConvexHull();
		return hull;
	}
		
	/** returns all points' positions as a String */
	public String toString() {
		String returnString = "Points:\n";
		for (int i=0; i<hull.npoints; i++){
			returnString = returnString + " Point " + i + ": (" +
				points.get(i).x + "," + points.get(i).y;
		}
		return returnString;
	}
	

	/** returns convex hull points */
	public String convexHullToString() {
		String hullPoints = "Convex Hull:\n";
		if (!hullCalculated)
			calculateConvexHull();
		for (int i=0; i<hull.npoints; i++){
			hullPoints = hullPoints + "\t(" + hull.xpoints[i] +"," 
				+ hull.ypoints[i] + ")\n";	
		}
		return hullPoints;
	}	
	 

	
	/**
	 * Calculates the convex hull from the current set of points
	 *
	 * This method currently does not work!
	 *
	 * You may NOT use the Polygon contains method in your final solution.
	 */
	private void calculateConvexHull() {
		hull.reset();
		hullCalculated = true;
		
		for (Point pt : points) {
			if (!hull.contains(pt))
				hull.addPoint(pt.x, pt.y);
		}
	}

	// extra credit method
	public Point[] getClosestPoints() {
		if (points.size() >= 2) {
			Point[] closest = new Point[2];
			closest[0] = points.get(0);
			closest[1] = points.get(1);
			return closest;
		}
		else 
			return null;
	}
}

