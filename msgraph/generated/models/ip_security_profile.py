from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
ip_category = lazy_import('msgraph.generated.models.ip_category')
ip_reference_data = lazy_import('msgraph.generated.models.ip_reference_data')
security_vendor_information = lazy_import('msgraph.generated.models.security_vendor_information')

class IpSecurityProfile(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
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
            value: Value to set for the activityGroupNames property.
        """
        self._activity_group_names = value
    
    @property
    def address(self,) -> Optional[str]:
        """
        Gets the address property value. The address property
        Returns: Optional[str]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[str] = None) -> None:
        """
        Sets the address property value. The address property
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
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
            value: Value to set for the azureSubscriptionId property.
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
            value: Value to set for the azureTenantId property.
        """
        self._azure_tenant_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ipSecurityProfile and sets the default values.
        """
        super().__init__()
        # The activityGroupNames property
        self._activity_group_names: Optional[List[str]] = None
        # The address property
        self._address: Optional[str] = None
        # The azureSubscriptionId property
        self._azure_subscription_id: Optional[str] = None
        # The azureTenantId property
        self._azure_tenant_id: Optional[str] = None
        # The countHits property
        self._count_hits: Optional[int] = None
        # The countHosts property
        self._count_hosts: Optional[int] = None
        # The firstSeenDateTime property
        self._first_seen_date_time: Optional[datetime] = None
        # The ipCategories property
        self._ip_categories: Optional[List[ip_category.IpCategory]] = None
        # The ipReferenceData property
        self._ip_reference_data: Optional[List[ip_reference_data.IpReferenceData]] = None
        # The lastSeenDateTime property
        self._last_seen_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The riskScore property
        self._risk_score: Optional[str] = None
        # The tags property
        self._tags: Optional[List[str]] = None
        # The vendorInformation property
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
    
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
            value: Value to set for the countHits property.
        """
        self._count_hits = value
    
    @property
    def count_hosts(self,) -> Optional[int]:
        """
        Gets the countHosts property value. The countHosts property
        Returns: Optional[int]
        """
        return self._count_hosts
    
    @count_hosts.setter
    def count_hosts(self,value: Optional[int] = None) -> None:
        """
        Sets the countHosts property value. The countHosts property
        Args:
            value: Value to set for the countHosts property.
        """
        self._count_hosts = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpSecurityProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpSecurityProfile()
    
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
            value: Value to set for the firstSeenDateTime property.
        """
        self._first_seen_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_group_names": lambda n : setattr(self, 'activity_group_names', n.get_collection_of_primitive_values(str)),
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "azure_subscription_id": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "count_hits": lambda n : setattr(self, 'count_hits', n.get_int_value()),
            "count_hosts": lambda n : setattr(self, 'count_hosts', n.get_int_value()),
            "first_seen_date_time": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "ip_categories": lambda n : setattr(self, 'ip_categories', n.get_collection_of_object_values(ip_category.IpCategory)),
            "ip_reference_data": lambda n : setattr(self, 'ip_reference_data', n.get_collection_of_object_values(ip_reference_data.IpReferenceData)),
            "last_seen_date_time": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ip_categories(self,) -> Optional[List[ip_category.IpCategory]]:
        """
        Gets the ipCategories property value. The ipCategories property
        Returns: Optional[List[ip_category.IpCategory]]
        """
        return self._ip_categories
    
    @ip_categories.setter
    def ip_categories(self,value: Optional[List[ip_category.IpCategory]] = None) -> None:
        """
        Sets the ipCategories property value. The ipCategories property
        Args:
            value: Value to set for the ipCategories property.
        """
        self._ip_categories = value
    
    @property
    def ip_reference_data(self,) -> Optional[List[ip_reference_data.IpReferenceData]]:
        """
        Gets the ipReferenceData property value. The ipReferenceData property
        Returns: Optional[List[ip_reference_data.IpReferenceData]]
        """
        return self._ip_reference_data
    
    @ip_reference_data.setter
    def ip_reference_data(self,value: Optional[List[ip_reference_data.IpReferenceData]] = None) -> None:
        """
        Sets the ipReferenceData property value. The ipReferenceData property
        Args:
            value: Value to set for the ipReferenceData property.
        """
        self._ip_reference_data = value
    
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
            value: Value to set for the lastSeenDateTime property.
        """
        self._last_seen_date_time = value
    
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
            value: Value to set for the riskScore property.
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
        writer.write_str_value("address", self.address)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_int_value("countHits", self.count_hits)
        writer.write_int_value("countHosts", self.count_hosts)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_collection_of_object_values("ipCategories", self.ip_categories)
        writer.write_collection_of_object_values("ipReferenceData", self.ip_reference_data)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
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
            value: Value to set for the vendorInformation property.
        """
        self._vendor_information = value
    

