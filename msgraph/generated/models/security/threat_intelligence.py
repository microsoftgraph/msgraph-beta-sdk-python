from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .article import Article
    from .article_indicator import ArticleIndicator
    from .host import Host
    from .host_component import HostComponent
    from .host_cookie import HostCookie
    from .host_pair import HostPair
    from .host_ssl_certificate import HostSslCertificate
    from .host_tracker import HostTracker
    from .intelligence_profile import IntelligenceProfile
    from .intelligence_profile_indicator import IntelligenceProfileIndicator
    from .passive_dns_record import PassiveDnsRecord
    from .ssl_certificate import SslCertificate
    from .subdomain import Subdomain
    from .vulnerability import Vulnerability
    from .whois_history_record import WhoisHistoryRecord
    from .whois_record import WhoisRecord

from ..entity import Entity

@dataclass
class ThreatIntelligence(Entity):
    # Refers to indicators of threat or compromise highlighted in an microsoft.graph.security.article.Note: List retrieval is not yet supported.
    article_indicators: Optional[List[ArticleIndicator]] = None
    # A list of article objects.
    articles: Optional[List[Article]] = None
    # Retrieve details about microsoft.graph.security.hostComponent objects.Note: List retrieval is not yet supported.
    host_components: Optional[List[HostComponent]] = None
    # Retrieve details about microsoft.graph.security.hostCookie objects.Note: List retrieval is not yet supported.
    host_cookies: Optional[List[HostCookie]] = None
    # Retrieve details about microsoft.graph.security.hostTracker objects.Note: List retrieval is not yet supported.
    host_pairs: Optional[List[HostPair]] = None
    # The hostSslCertificates property
    host_ssl_certificates: Optional[List[HostSslCertificate]] = None
    # Retrieve details about microsoft.graph.security.hostTracker objects.Note: List retrieval is not yet supported.
    host_trackers: Optional[List[HostTracker]] = None
    # Refers to microsoft.graph.security.host objects that Microsoft Threat Intelligence has observed.Note: List retrieval is not yet supported.
    hosts: Optional[List[Host]] = None
    # A list of intelligenceProfile objects.
    intel_profiles: Optional[List[IntelligenceProfile]] = None
    # The intelligenceProfileIndicators property
    intelligence_profile_indicators: Optional[List[IntelligenceProfileIndicator]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Retrieve details about microsoft.graph.security.passiveDnsRecord objects.Note: List retrieval is not yet supported.
    passive_dns_records: Optional[List[PassiveDnsRecord]] = None
    # The sslCertificates property
    ssl_certificates: Optional[List[SslCertificate]] = None
    # Retrieve details about the microsoft.graph.security.subdomain.Note: List retrieval is not yet supported.
    subdomains: Optional[List[Subdomain]] = None
    # Retrieve details about microsoft.graph.security.vulnerabilities.Note: List retrieval is not yet supported.
    vulnerabilities: Optional[List[Vulnerability]] = None
    # The whoisHistoryRecords property
    whois_history_records: Optional[List[WhoisHistoryRecord]] = None
    # The whoisRecords property
    whois_records: Optional[List[WhoisRecord]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatIntelligence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThreatIntelligence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ThreatIntelligence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .article import Article
        from .article_indicator import ArticleIndicator
        from .host import Host
        from .host_component import HostComponent
        from .host_cookie import HostCookie
        from .host_pair import HostPair
        from .host_ssl_certificate import HostSslCertificate
        from .host_tracker import HostTracker
        from .intelligence_profile import IntelligenceProfile
        from .intelligence_profile_indicator import IntelligenceProfileIndicator
        from .passive_dns_record import PassiveDnsRecord
        from .ssl_certificate import SslCertificate
        from .subdomain import Subdomain
        from .vulnerability import Vulnerability
        from .whois_history_record import WhoisHistoryRecord
        from .whois_record import WhoisRecord

        from ..entity import Entity
        from .article import Article
        from .article_indicator import ArticleIndicator
        from .host import Host
        from .host_component import HostComponent
        from .host_cookie import HostCookie
        from .host_pair import HostPair
        from .host_ssl_certificate import HostSslCertificate
        from .host_tracker import HostTracker
        from .intelligence_profile import IntelligenceProfile
        from .intelligence_profile_indicator import IntelligenceProfileIndicator
        from .passive_dns_record import PassiveDnsRecord
        from .ssl_certificate import SslCertificate
        from .subdomain import Subdomain
        from .vulnerability import Vulnerability
        from .whois_history_record import WhoisHistoryRecord
        from .whois_record import WhoisRecord

        fields: Dict[str, Callable[[Any], None]] = {
            "articleIndicators": lambda n : setattr(self, 'article_indicators', n.get_collection_of_object_values(ArticleIndicator)),
            "articles": lambda n : setattr(self, 'articles', n.get_collection_of_object_values(Article)),
            "hostComponents": lambda n : setattr(self, 'host_components', n.get_collection_of_object_values(HostComponent)),
            "hostCookies": lambda n : setattr(self, 'host_cookies', n.get_collection_of_object_values(HostCookie)),
            "hostPairs": lambda n : setattr(self, 'host_pairs', n.get_collection_of_object_values(HostPair)),
            "hostSslCertificates": lambda n : setattr(self, 'host_ssl_certificates', n.get_collection_of_object_values(HostSslCertificate)),
            "hostTrackers": lambda n : setattr(self, 'host_trackers', n.get_collection_of_object_values(HostTracker)),
            "hosts": lambda n : setattr(self, 'hosts', n.get_collection_of_object_values(Host)),
            "intelProfiles": lambda n : setattr(self, 'intel_profiles', n.get_collection_of_object_values(IntelligenceProfile)),
            "intelligenceProfileIndicators": lambda n : setattr(self, 'intelligence_profile_indicators', n.get_collection_of_object_values(IntelligenceProfileIndicator)),
            "passiveDnsRecords": lambda n : setattr(self, 'passive_dns_records', n.get_collection_of_object_values(PassiveDnsRecord)),
            "sslCertificates": lambda n : setattr(self, 'ssl_certificates', n.get_collection_of_object_values(SslCertificate)),
            "subdomains": lambda n : setattr(self, 'subdomains', n.get_collection_of_object_values(Subdomain)),
            "vulnerabilities": lambda n : setattr(self, 'vulnerabilities', n.get_collection_of_object_values(Vulnerability)),
            "whoisHistoryRecords": lambda n : setattr(self, 'whois_history_records', n.get_collection_of_object_values(WhoisHistoryRecord)),
            "whoisRecords": lambda n : setattr(self, 'whois_records', n.get_collection_of_object_values(WhoisRecord)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("articleIndicators", self.article_indicators)
        writer.write_collection_of_object_values("articles", self.articles)
        writer.write_collection_of_object_values("hostComponents", self.host_components)
        writer.write_collection_of_object_values("hostCookies", self.host_cookies)
        writer.write_collection_of_object_values("hostPairs", self.host_pairs)
        writer.write_collection_of_object_values("hostSslCertificates", self.host_ssl_certificates)
        writer.write_collection_of_object_values("hostTrackers", self.host_trackers)
        writer.write_collection_of_object_values("hosts", self.hosts)
        writer.write_collection_of_object_values("intelProfiles", self.intel_profiles)
        writer.write_collection_of_object_values("intelligenceProfileIndicators", self.intelligence_profile_indicators)
        writer.write_collection_of_object_values("passiveDnsRecords", self.passive_dns_records)
        writer.write_collection_of_object_values("sslCertificates", self.ssl_certificates)
        writer.write_collection_of_object_values("subdomains", self.subdomains)
        writer.write_collection_of_object_values("vulnerabilities", self.vulnerabilities)
        writer.write_collection_of_object_values("whoisHistoryRecords", self.whois_history_records)
        writer.write_collection_of_object_values("whoisRecords", self.whois_records)
    

