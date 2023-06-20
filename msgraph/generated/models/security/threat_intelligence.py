from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import article, article_indicator, host, host_component, host_cookie, host_tracker, intelligence_profile, intelligence_profile_indicator, passive_dns_record, vulnerability
    from .. import entity

from .. import entity

@dataclass
class ThreatIntelligence(entity.Entity):
    # Refers to indicators of threat or compromise highlighted in an microsoft.graph.security.article.Note: List retrieval is not yet supported.
    article_indicators: Optional[List[article_indicator.ArticleIndicator]] = None
    # A list of article objects.
    articles: Optional[List[article.Article]] = None
    # Retrieve details about microsoft.graph.security.hostComponent objects.Note: List retrieval is not yet supported.
    host_components: Optional[List[host_component.HostComponent]] = None
    # Retrieve details about microsoft.graph.security.hostCookie objects.Note: List retrieval is not yet supported.
    host_cookies: Optional[List[host_cookie.HostCookie]] = None
    # Retrieve details about microsoft.graph.security.hostTracker objects.Note: List retrieval is not yet supported.
    host_trackers: Optional[List[host_tracker.HostTracker]] = None
    # Refers to microsoft.graph.security.host objects that Microsoft Threat Intelligence has observed.Note: List retrieval is not yet supported.
    hosts: Optional[List[host.Host]] = None
    # A list of intelligenceProfile objects.
    intel_profiles: Optional[List[intelligence_profile.IntelligenceProfile]] = None
    # The intelligenceProfileIndicators property
    intelligence_profile_indicators: Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Retrieve details about microsoft.graph.security.passiveDnsRecord objects.Note: List retrieval is not yet supported.
    passive_dns_records: Optional[List[passive_dns_record.PassiveDnsRecord]] = None
    # Retrieve details about microsoft.graph.security.vulnerabilities.Note: List retrieval is not yet supported.
    vulnerabilities: Optional[List[vulnerability.Vulnerability]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatIntelligence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import article, article_indicator, host, host_component, host_cookie, host_tracker, intelligence_profile, intelligence_profile_indicator, passive_dns_record, vulnerability
        from .. import entity

        from . import article, article_indicator, host, host_component, host_cookie, host_tracker, intelligence_profile, intelligence_profile_indicator, passive_dns_record, vulnerability
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "articleIndicators": lambda n : setattr(self, 'article_indicators', n.get_collection_of_object_values(article_indicator.ArticleIndicator)),
            "articles": lambda n : setattr(self, 'articles', n.get_collection_of_object_values(article.Article)),
            "hostComponents": lambda n : setattr(self, 'host_components', n.get_collection_of_object_values(host_component.HostComponent)),
            "hostCookies": lambda n : setattr(self, 'host_cookies', n.get_collection_of_object_values(host_cookie.HostCookie)),
            "hostTrackers": lambda n : setattr(self, 'host_trackers', n.get_collection_of_object_values(host_tracker.HostTracker)),
            "hosts": lambda n : setattr(self, 'hosts', n.get_collection_of_object_values(host.Host)),
            "intelProfiles": lambda n : setattr(self, 'intel_profiles', n.get_collection_of_object_values(intelligence_profile.IntelligenceProfile)),
            "intelligenceProfileIndicators": lambda n : setattr(self, 'intelligence_profile_indicators', n.get_collection_of_object_values(intelligence_profile_indicator.IntelligenceProfileIndicator)),
            "passiveDnsRecords": lambda n : setattr(self, 'passive_dns_records', n.get_collection_of_object_values(passive_dns_record.PassiveDnsRecord)),
            "vulnerabilities": lambda n : setattr(self, 'vulnerabilities', n.get_collection_of_object_values(vulnerability.Vulnerability)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("articleIndicators", self.article_indicators)
        writer.write_collection_of_object_values("articles", self.articles)
        writer.write_collection_of_object_values("hostComponents", self.host_components)
        writer.write_collection_of_object_values("hostCookies", self.host_cookies)
        writer.write_collection_of_object_values("hostTrackers", self.host_trackers)
        writer.write_collection_of_object_values("hosts", self.hosts)
        writer.write_collection_of_object_values("intelProfiles", self.intel_profiles)
        writer.write_collection_of_object_values("intelligenceProfileIndicators", self.intelligence_profile_indicators)
        writer.write_collection_of_object_values("passiveDnsRecords", self.passive_dns_records)
        writer.write_collection_of_object_values("vulnerabilities", self.vulnerabilities)
    

