from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import domain_registrant, entity, reputation_category, security_vendor_information

from . import entity

class DomainSecurityProfile(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DomainSecurityProfile and sets the default values.
        """
        super().__init__()
        # The activityGroupNames property
        self._activity_group_names: Optional[List[str]] = None
        # The azureSubscriptionId property
        self._azure_subscription_id: Optional[str] = None
        # The azureTenantId property
        self._azure_tenant_id: Optional[str] = None
        # The countHits property
        self._count_hits: Optional[int] = None
        # The countInOrg property
        self._count_in_org: Optional[int] = None
        # The domainCategories property
        self._domain_categories: Optional[List[reputation_category.ReputationCategory]] = None
        # The domainRegisteredDateTime property
        self._domain_registered_date_time: Optional[datetime] = None
        # The firstSeenDateTime property
        self._first_seen_date_time: Optional[datetime] = None
        # The lastSeenDateTime property
        self._last_seen_date_time: Optional[datetime] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The registrant property
        self._registrant: Optional[domain_registrant.DomainRegistrant] = None
        # The riskScore property
        self._risk_score: Optional[str] = None
        # The tags property
        self._tags: Optional[List[str]] = None
        # The vendorInformation property
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
    
    @property
    def activity_group_names(self,) -> Optional[List[str]]:
        """
        Gets the activityGroupNames property value. The activityGroupNames property
        Returns: Optional[List[str]]
        """
        return self._activity_group_names
    
    @activity_group_names.setter
    def activity_group_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the activityGroupNames property value. The activityGroupNames property
        Args:
            value: Value to set for the activity_group_names property.
        """
        self._activity_group_names = value
    
    @property
    def azure_subscription_id(self,) -> Optional[str]:
        """
        Gets the azureSubscriptionId property value. The azureSubscriptionId property
        Returns: Optional[str]
        """
        return self._azure_subscription_id
    
    @azure_subscription_id.setter
    def azure_subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureSubscriptionId property value. The azureSubscriptionId property
        Args:
            value: Value to set for the azure_subscription_id property.
        """
        self._azure_subscription_id = value
    
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. The azureTenantId property
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. The azureTenantId property
        Args:
            value: Value to set for the azure_tenant_id property.
        """
        self._azure_tenant_id = value
    
    @property
    def count_hits(self,) -> Optional[int]:
        """
        Gets the countHits property value. The countHits property
        Returns: Optional[int]
        """
        return self._count_hits
    
    @count_hits.setter
    def count_hits(self,value: Optional[int] = None) -> None:
        """
        Sets the countHits property value. The countHits property
        Args:
            value: Value to set for the count_hits property.
        """
        self._count_hits = value
    
    @property
    def count_in_org(self,) -> Optional[int]:
        """
        Gets the countInOrg property value. The countInOrg property
        Returns: Optional[int]
        """
        return self._count_in_org
    
    @count_in_org.setter
    def count_in_org(self,value: Optional[int] = None) -> None:
        """
        Sets the countInOrg property value. The countInOrg property
        Args:
            value: Value to set for the count_in_org property.
        """
        self._count_in_org = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainSecurityProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DomainSecurityProfile()
    
    @property
    def domain_categories(self,) -> Optional[List[reputation_category.ReputationCategory]]:
        """
        Gets the domainCategories property value. The domainCategories property
        Returns: Optional[List[reputation_category.ReputationCategory]]
        """
        return self._domain_categories
    
    @domain_categories.setter
    def domain_categories(self,value: Optional[List[reputation_category.ReputationCategory]] = None) -> None:
        """
        Sets the domainCategories property value. The domainCategories property
        Args:
            value: Value to set for the domain_categories property.
        """
        self._domain_categories = value
    
    @property
    def domain_registered_date_time(self,) -> Optional[datetime]:
        """
        Gets the domainRegisteredDateTime property value. The domainRegisteredDateTime property
        Returns: Optional[datetime]
        """
        return self._domain_registered_date_time
    
    @domain_registered_date_time.setter
    def domain_registered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the domainRegisteredDateTime property value. The domainRegisteredDateTime property
        Args:
            value: Value to set for the domain_registered_date_time property.
        """
        self._domain_registered_date_time = value
    
    @property
    def first_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstSeenDateTime property value. The firstSeenDateTime property
        Returns: Optional[datetime]
        """
        return self._first_seen_date_time
    
    @first_seen_date_time.setter
    def first_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstSeenDateTime property value. The firstSeenDateTime property
        Args:
            value: Value to set for the first_seen_date_time property.
        """
        self._first_seen_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import domain_registrant, entity, reputation_category, security_vendor_information

        fields: Dict[str, Callable[[Any], None]] = {
            "activityGroupNames": lambda n : setattr(self, 'activity_group_names', n.get_collection_of_primitive_values(str)),
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "countHits": lambda n : setattr(self, 'count_hits', n.get_int_value()),
            "countInOrg": lambda n : setattr(self, 'count_in_org', n.get_int_value()),
            "domainCategories": lambda n : setattr(self, 'domain_categories', n.get_collection_of_object_values(reputation_category.ReputationCategory)),
            "domainRegisteredDateTime": lambda n : setattr(self, 'domain_registered_date_time', n.get_datetime_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "registrant": lambda n : setattr(self, 'registrant', n.get_object_value(domain_registrant.DomainRegistrant)),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSeenDateTime property value. The lastSeenDateTime property
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. The lastSeenDateTime property
        Args:
            value: Value to set for the last_seen_date_time property.
        """
        self._last_seen_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def registrant(self,) -> Optional[domain_registrant.DomainRegistrant]:
        """
        Gets the registrant property value. The registrant property
        Returns: Optional[domain_registrant.DomainRegistrant]
        """
        return self._registrant
    
    @registrant.setter
    def registrant(self,value: Optional[domain_registrant.DomainRegistrant] = None) -> None:
        """
        Sets the registrant property value. The registrant property
        Args:
            value: Value to set for the registrant property.
        """
        self._registrant = value
    
    @property
    def risk_score(self,) -> Optional[str]:
        """
        Gets the riskScore property value. The riskScore property
        Returns: Optional[str]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[str] = None) -> None:
        """
        Sets the riskScore property value. The riskScore property
        Args:
            value: Value to set for the risk_score property.
        """
        self._risk_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("activityGroupNames", self.activity_group_names)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_int_value("countHits", self.count_hits)
        writer.write_int_value("countInOrg", self.count_in_org)
        writer.write_collection_of_object_values("domainCategories", self.domain_categories)
        writer.write_datetime_value("domainRegisteredDateTime", self.domain_registered_date_time)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("registrant", self.registrant)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("vendorInformation", self.vendor_information)
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. The tags property
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. The tags property
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def vendor_information(self,) -> Optional[security_vendor_information.SecurityVendorInformation]:
        """
        Gets the vendorInformation property value. The vendorInformation property
        Returns: Optional[security_vendor_information.SecurityVendorInformation]
        """
        return self._vendor_information
    
    @vendor_information.setter
    def vendor_information(self,value: Optional[security_vendor_information.SecurityVendorInformation] = None) -> None:
        """
        Sets the vendorInformation property value. The vendorInformation property
        Args:
            value: Value to set for the vendor_information property.
        """
        self._vendor_information = value
    

