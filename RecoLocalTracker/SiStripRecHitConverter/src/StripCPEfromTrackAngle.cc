#include "RecoLocalTracker/SiStripRecHitConverter/interface/StripCPEfromTrackAngle.h"
#include "Geometry/CommonTopologies/interface/StripTopology.h"                                                           


namespace {
  inline
  float stripErrorSquared(const unsigned N, const float uProj) {
    if( (float(N)-uProj) > 3.5f )  
      return float(N*N)/12.f;
    else {
      const float P1=-0.339f;
      const float P2=0.90f;
      const float P3=0.279f;
      const float uerr = P1*uProj*std::exp(-uProj*P2)+P3;
      return uerr*uerr;
    }
  }
}

StripClusterParameterEstimator::LocalValues StripCPEfromTrackAngle::
localParameters( const SiStripCluster& cluster, const GeomDetUnit& det, const LocalTrajectoryParameters& ltp) const {
  
  StripCPE::Param const & p = param(det);
  
  LocalVector track = ltp.momentum();
  track *= 
    (track.z()<0) ?  std::abs(p.thickness/track.z()) : 
    (track.z()>0) ? -std::abs(p.thickness/track.z()) :  
                         p.maxLength/track.mag() ;

  const unsigned N = cluster.amplitudes().size();
  const float fullProjection = p.coveredStrips( track+p.drift, ltp.position());
  const float uerr2 = stripErrorSquared( N, std::abs(fullProjection) );
  const float strip = cluster.barycenter() -  0.5f*(1.f-shift[p.moduleGeom]) * fullProjection
    + 0.5f*p.coveredStrips(track, ltp.position());
  //std::cout<<"TRACK ANGLE"<< std::endl;
  return std::make_pair( p.topology->localPosition(strip, ltp.vector()),
			 p.topology->localError(strip, uerr2, ltp.vector()) );
}

