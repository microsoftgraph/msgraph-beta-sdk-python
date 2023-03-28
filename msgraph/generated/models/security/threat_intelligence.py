from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import article, article_indicator, host, host_component, host_cookie, host_tracker, intelligence_profile, intelligence_profile_indicator, passive_dns_record, vulnerability
    from .. import entity

from .. import entity

class ThreatIntelligence(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new threatIntelligence and sets the default values.
        """
        super().__init__()
        # Refers to indicators of threat or compromise highlighted in an microsoft.graph.security.article.Note: List retrieval is not yet supported.
        self._article_indicators: Optional[List[article_indicator.ArticleIndicator]] = None
        # A list of article objects.
        self._articles: Optional[List[article.Article]] = None
        # Retrieve details about microsoft.graph.security.hostComponent objects.Note: List retrieval is not yet supported.
        self._host_components: Optional[List[host_component.HostComponent]] = None
        # Retrieve details about microsoft.graph.security.hostCookie objects.Note: List retrieval is not yet supported.
        self._host_cookies: Optional[List[host_cookie.HostCookie]] = None
        # Retrieve details about microsoft.graph.security.hostTracker objects.Note: List retrieval is not yet supported.
        self._host_trackers: Optional[List[host_tracker.HostTracker]] = None
        # Refers to microsoft.graph.security.host objects that Microsoft Threat Intelligence has observed.Note: List retrieval is not yet supported.
        self._hosts: Optional[List[host.Host]] = None
        # A list of intelligenceProfile objects.
        self._intel_profiles: Optional[List[intelligence_profile.IntelligenceProfile]] = None
        # The intelligenceProfileIndicators property
        self._intelligence_profile_indicators: Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Retrieve details about microsoft.graph.security.passiveDnsRecord objects.Note: List retrieval is not yet supported.
        self._passive_dns_records: Optional[List[passive_dns_record.PassiveDnsRecord]] = None
        # Retrieve details about microsoft.graph.security.vulnerabilities.Note: List retrieval is not yet supported.
        self._vulnerabilities: Optional[List[vulnerability.Vulnerability]] = None
    
    @property
    def article_indicators(self,) -> Optional[List[article_indicator.ArticleIndicator]]:
        """
        Gets the articleIndicators property value. Refers to indicators of threat or compromise highlighted in an microsoft.graph.security.article.Note: List retrieval is not yet supported.
        Returns: Optional[List[article_indicator.ArticleIndicator]]
        """
        return self._article_indicators
    
    @article_indicators.setter
    def article_indicators(self,value: Optional[List[article_indicator.ArticleIndicator]] = None) -> None:
        """
        Sets the articleIndicators property value. Refers to indicators of threat or compromise highlighted in an microsoft.graph.security.article.Note: List retrieval is not yet supported.
        Args:
            value: Value to set for the article_indicators property.
        """
        self._article_indicators = value
    
    @property
    def articles(self,) -> Optional[List[article.Article]]:
        """
        Gets the articles property value. A list of article objects.
        Returns: Optional[List[article.Article]]
        """
        return self._articles
    
    @articles.setter
    def articles(self,value: Optional[List[article.Article]] = None) -> None:
        """
        Sets the articles property value. A list of article objects.
        Args:
            value: Value to set for the articles property.
        """
        self._articles = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatIntelligence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatIntelligence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ThreatIntelligence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import article, article_indicator, host, host_component, host_cookie, host_tracker, intelligence_profile, intelligence_profile_indicator, passive_dns_record, vulnerability
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "articles": lambda n : setattr(self, 'articles', n.get_collection_of_object_values(article.Article)),
            "articleIndicators": lambda n : setattr(self, 'article_indicators', n.get_collection_of_object_values(article_indicator.ArticleIndicator)),
            "hosts": lambda n : setattr(self, 'hosts', n.get_collection_of_object_values(host.Host)),
            "hostComponents": lambda n : setattr(self, 'host_components', n.get_collection_of_object_values(host_component.HostComponent)),
            "hostCookies": lambda n : setattr(self, 'host_cookies', n.get_collection_of_object_values(host_cookie.HostCookie)),
            "hostTrackers": lambda n : setattr(self, 'host_trackers', n.get_collection_of_object_values(host_tracker.HostTracker)),
            "intelligenceProfileIndicators": lambda n : setattr(self, 'intelligence_profile_indicators', n.get_collection_of_object_values(intelligence_profile_indicator.IntelligenceProfileIndicator)),
            "intelProfiles": lambda n : setattr(self, 'intel_profiles', n.get_collection_of_object_values(intelligence_profile.IntelligenceProfile)),
            "passiveDnsRecords": lambda n : setattr(self, 'passive_dns_records', n.get_collection_of_object_values(passive_dns_record.PassiveDnsRecord)),
            "vulnerabilities": lambda n : setattr(self, 'vulnerabilities', n.get_collection_of_object_values(vulnerability.Vulnerability)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host_components(self,) -> Optional[List[host_component.HostComponent]]:
        """
        Gets the hostComponents property value. Retrieve details about microsoft.graph.security.hostComponent objects.Note: List retrieval is not yet supported.
        Returns: Optional[List[host_component.HostComponent]]
        """
        return self._host_components
    
    @host_components.setter
    def host_components(self,value: Optional[List[host_component.HostComponent]] = None) -> None:
        """
        Sets the hostComponents property value. Retrieve details about microsoft.graph.security.hostComponent objects.Note: List retrieval is not yet supported.
        Args:
            value: Value to set for the host_components property.
        """
        self._host_components = value
    
    @property
    def host_cookies(self,) -> Optional[List[host_cookie.HostCookie]]:
        """
        Gets the hostCookies property value. Retrieve details about microsoft.graph.security.hostCookie objects.Note: List retrieval is not yet supported.
        Returns: Optional[List[host_cookie.HostCookie]]
        """
        return self._host_cookies
    
    @host_cookies.setter
    def host_cookies(self,value: Optional[List[host_cookie.HostCookie]] = None) -> None:
        """
        Sets the hostCookies property value. Retrieve details about microsoft.graph.security.hostCookie objects.Note: List retrieval is not yet supported.
        Args:
            value: Value to set for the host_cookies property.
        """
        self._host_cookies = value
    
    @property
    def host_trackers(self,) -> Optional[List[host_tracker.HostTracker]]:
        """
        Gets the hostTrackers property value. Retrieve details about microsoft.graph.security.hostTracker objects.Note: List retrieval is not yet supported.
        Returns: Optional[List[host_tracker.HostTracker]]
        """
        return self._host_trackers
    
    @host_trackers.setter
    def host_trackers(self,value: Optional[List[host_tracker.HostTracker]] = None) -> None:
        """
        Sets the hostTrackers property value. Retrieve details about microsoft.graph.security.hostTracker objects.Note: List retrieval is not yet supported.
        Args:
            value: Value to set for the host_trackers property.
        """
        self._host_trackers = value
    
    @property
    def hosts(self,) -> Optional[List[host.Host]]:
        """
        Gets the hosts property value. Refers to microsoft.graph.security.host objects that Microsoft Threat Intelligence has observed.Note: List retrieval is not yet supported.
        Returns: Optional[List[host.Host]]
        """
        return self._hosts
    
    @hosts.setter
    def hosts(self,value: Optional[List[host.Host]] = None) -> None:
        """
        Sets the hosts property value. Refers to microsoft.graph.security.host objects that Microsoft Threat Intelligence has observed.Note: List retrieval is not yet supported.
        Args:
            value: Value to set for the hosts property.
        """
        self._hosts = value
    
    @property
    def intel_profiles(self,) -> Optional[List[intelligence_profile.IntelligenceProfile]]:
        """
        Gets the intelProfiles property value. A list of intelligenceProfile objects.
        Returns: Optional[List[intelligence_profile.IntelligenceProfile]]
        """
        return self._intel_profiles
    
    @intel_profiles.setter
    def intel_profiles(self,value: Optional[List[intelligence_profile.IntelligenceProfile]] = None) -> None:
        """
        Sets the intelProfiles property value. A list of intelligenceProfile objects.
        Args:
            value: Value to set for the intel_profiles property.
        """
        self._intel_profiles = value
    
    @property
    def intelligence_profile_indicators(self,) -> Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]]:
        """
        Gets the intelligenceProfileIndicators property value. The intelligenceProfileIndicators property
        Returns: Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]]
        """
        return self._intelligence_profile_indicators
    
    @intelligence_profile_indicators.setter
    def intelligence_profile_indicators(self,value: Optional[List[intelligence_profile_indicator.IntelligenceProfileIndicator]] = None) -> None:
        """
        Sets the intelligenceProfileIndicators property value. The intelligenceProfileIndicators property
        Args:
            value: Value to set for the intelligence_profile_indicators property.
        """
        self._intelligence_profile_indicators = value
    
    @property
    def passive_dns_records(self,) -> Optional[List[passive_dns_record.PassiveDnsRecord]]:
        """
        Gets the passiveDnsRecords property value. Retrieve details about microsoft.graph.security.passiveDnsRecord objects.Note: List retrieval is not yet supported.
        Returns: Optional[List[passive_dns_record.PassiveDnsRecord]]
        """
        return self._passive_dns_records
    
    @passive_dns_records.setter
    def passive_dns_records(self,value: Optional[List[passive_dns_record.PassiveDnsRecord]] = None) -> None:
        """
        Sets the passiveDnsRecords property value. Retrieve details about microsoft.graph.security.passiveDnsRecord objects.Note: List retrieval is not yet supported.
        Args:
            value: Value to set for the passive_dns_records property.
        """
        self._passive_dns_records = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("articles", self.articles)
        writer.write_collection_of_object_values("articleIndicators", self.article_indicators)
        writer.write_collection_of_object_values("hosts", self.hosts)
        writer.write_collection_of_object_values("hostComponents", self.host_components)
        writer.write_collection_of_object_values("hostCookies", self.host_cookies)
        writer.write_collection_of_object_values("hostTrackers", self.host_trackers)
        writer.write_collection_of_object_values("intelligenceProfileIndicators", self.intelligence_profile_indicators)
        writer.write_collection_of_object_values("intelProfiles", self.intel_profiles)
        writer.write_collection_of_object_values("passiveDnsRecords", self.passive_dns_records)
        writer.write_collection_of_object_values("vulnerabilities", self.vulnerabilities)
    
    @property
    def vulnerabilities(self,) -> Optional[List[vulnerability.Vulnerability]]:
        """
        Gets the vulnerabilities property value. Retrieve details about microsoft.graph.security.vulnerabilities.Note: List retrieval is not yet supported.
        Returns: Optional[List[vulnerability.Vulnerability]]
        """
        return self._vulnerabilities
    
    @vulnerabilities.setter
    def vulnerabilities(self,value: Optional[List[vulnerability.Vulnerability]] = None) -> None:
        """
        Sets the vulnerabilities property value. Retrieve details about microsoft.graph.security.vulnerabilities.Note: List retrieval is not yet supported.
        Args:
            value: Value to set for the vulnerabilities property.
        """
        self._vulnerabilities = value
    

