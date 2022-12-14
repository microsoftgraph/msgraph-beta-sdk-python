from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
file_hash = lazy_import('msgraph.generated.models.file_hash')
malware_state = lazy_import('msgraph.generated.models.malware_state')
security_vendor_information = lazy_import('msgraph.generated.models.security_vendor_information')
vulnerability_state = lazy_import('msgraph.generated.models.vulnerability_state')

class FileSecurityProfile(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
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
    
    @property
    def certificate_thumbprint(self,) -> Optional[str]:
        """
        Gets the certificateThumbprint property value. The certificateThumbprint property
        Returns: Optional[str]
        """
        return self._certificate_thumbprint
    
    @certificate_thumbprint.setter
    def certificate_thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateThumbprint property value. The certificateThumbprint property
        Args:
            value: Value to set for the certificateThumbprint property.
        """
        self._certificate_thumbprint = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new fileSecurityProfile and sets the default values.
        """
        super().__init__()
        # The activityGroupNames property
        self._activity_group_names: Optional[List[str]] = None
        # The azureSubscriptionId property
        self._azure_subscription_id: Optional[str] = None
        # The azureTenantId property
        self._azure_tenant_id: Optional[str] = None
        # The certificateThumbprint property
        self._certificate_thumbprint: Optional[str] = None
        # The extensions property
        self._extensions: Optional[List[str]] = None
        # The fileType property
        self._file_type: Optional[str] = None
        # The firstSeenDateTime property
        self._first_seen_date_time: Optional[datetime] = None
        # The hashes property
        self._hashes: Optional[List[file_hash.FileHash]] = None
        # The lastSeenDateTime property
        self._last_seen_date_time: Optional[datetime] = None
        # The malwareStates property
        self._malware_states: Optional[List[malware_state.MalwareState]] = None
        # The names property
        self._names: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The riskScore property
        self._risk_score: Optional[str] = None
        # The size property
        self._size: Optional[int] = None
        # The tags property
        self._tags: Optional[List[str]] = None
        # The vendorInformation property
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
        # The vulnerabilityStates property
        self._vulnerability_states: Optional[List[vulnerability_state.VulnerabilityState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileSecurityProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileSecurityProfile()
    
    @property
    def extensions(self,) -> Optional[List[str]]:
        """
        Gets the extensions property value. The extensions property
        Returns: Optional[List[str]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the extensions property value. The extensions property
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    @property
    def file_type(self,) -> Optional[str]:
        """
        Gets the fileType property value. The fileType property
        Returns: Optional[str]
        """
        return self._file_type
    
    @file_type.setter
    def file_type(self,value: Optional[str] = None) -> None:
        """
        Sets the fileType property value. The fileType property
        Args:
            value: Value to set for the fileType property.
        """
        self._file_type = value
    
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
            "azure_subscription_id": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "certificate_thumbprint": lambda n : setattr(self, 'certificate_thumbprint', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_primitive_values(str)),
            "file_type": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "first_seen_date_time": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "hashes": lambda n : setattr(self, 'hashes', n.get_collection_of_object_values(file_hash.FileHash)),
            "last_seen_date_time": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "malware_states": lambda n : setattr(self, 'malware_states', n.get_collection_of_object_values(malware_state.MalwareState)),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_primitive_values(str)),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
            "vulnerability_states": lambda n : setattr(self, 'vulnerability_states', n.get_collection_of_object_values(vulnerability_state.VulnerabilityState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hashes(self,) -> Optional[List[file_hash.FileHash]]:
        """
        Gets the hashes property value. The hashes property
        Returns: Optional[List[file_hash.FileHash]]
        """
        return self._hashes
    
    @hashes.setter
    def hashes(self,value: Optional[List[file_hash.FileHash]] = None) -> None:
        """
        Sets the hashes property value. The hashes property
        Args:
            value: Value to set for the hashes property.
        """
        self._hashes = value
    
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
    def malware_states(self,) -> Optional[List[malware_state.MalwareState]]:
        """
        Gets the malwareStates property value. The malwareStates property
        Returns: Optional[List[malware_state.MalwareState]]
        """
        return self._malware_states
    
    @malware_states.setter
    def malware_states(self,value: Optional[List[malware_state.MalwareState]] = None) -> None:
        """
        Sets the malwareStates property value. The malwareStates property
        Args:
            value: Value to set for the malwareStates property.
        """
        self._malware_states = value
    
    @property
    def names(self,) -> Optional[List[str]]:
        """
        Gets the names property value. The names property
        Returns: Optional[List[str]]
        """
        return self._names
    
    @names.setter
    def names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the names property value. The names property
        Args:
            value: Value to set for the names property.
        """
        self._names = value
    
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
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_str_value("certificateThumbprint", self.certificate_thumbprint)
        writer.write_collection_of_primitive_values("extensions", self.extensions)
        writer.write_str_value("fileType", self.file_type)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_collection_of_object_values("hashes", self.hashes)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("malwareStates", self.malware_states)
        writer.write_collection_of_primitive_values("names", self.names)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_int_value("size", self.size)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("vendorInformation", self.vendor_information)
        writer.write_collection_of_object_values("vulnerabilityStates", self.vulnerability_states)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The size property
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The size property
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
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
    
    @property
    def vulnerability_states(self,) -> Optional[List[vulnerability_state.VulnerabilityState]]:
        """
        Gets the vulnerabilityStates property value. The vulnerabilityStates property
        Returns: Optional[List[vulnerability_state.VulnerabilityState]]
        """
        return self._vulnerability_states
    
    @vulnerability_states.setter
    def vulnerability_states(self,value: Optional[List[vulnerability_state.VulnerabilityState]] = None) -> None:
        """
        Sets the vulnerabilityStates property value. The vulnerabilityStates property
        Args:
            value: Value to set for the vulnerabilityStates property.
        """
        self._vulnerability_states = value
    

