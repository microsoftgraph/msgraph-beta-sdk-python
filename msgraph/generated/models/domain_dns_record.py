from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import domain_dns_cname_record, domain_dns_mx_record, domain_dns_srv_record, domain_dns_txt_record, domain_dns_unavailable_record, entity

from . import entity

class DomainDnsRecord(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new domainDnsRecord and sets the default values.
        """
        super().__init__()
        # If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.
        self._is_optional: Optional[bool] = None
        # Value used when configuring the name of the DNS record at the DNS host.
        self._label: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, Txt.
        self._record_type: Optional[str] = None
        # Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune.
        self._supported_service: Optional[str] = None
        # Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable.
        self._ttl: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainDnsRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.domainDnsCnameRecord":
                from . import domain_dns_cname_record

                return domain_dns_cname_record.DomainDnsCnameRecord()
            if mapping_value == "#microsoft.graph.domainDnsMxRecord":
                from . import domain_dns_mx_record

                return domain_dns_mx_record.DomainDnsMxRecord()
            if mapping_value == "#microsoft.graph.domainDnsSrvRecord":
                from . import domain_dns_srv_record

                return domain_dns_srv_record.DomainDnsSrvRecord()
            if mapping_value == "#microsoft.graph.domainDnsTxtRecord":
                from . import domain_dns_txt_record

                return domain_dns_txt_record.DomainDnsTxtRecord()
            if mapping_value == "#microsoft.graph.domainDnsUnavailableRecord":
                from . import domain_dns_unavailable_record

                return domain_dns_unavailable_record.DomainDnsUnavailableRecord()
        return DomainDnsRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import domain_dns_cname_record, domain_dns_mx_record, domain_dns_srv_record, domain_dns_txt_record, domain_dns_unavailable_record, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "isOptional": lambda n : setattr(self, 'is_optional', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "recordType": lambda n : setattr(self, 'record_type', n.get_str_value()),
            "supportedService": lambda n : setattr(self, 'supported_service', n.get_str_value()),
            "ttl": lambda n : setattr(self, 'ttl', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_optional(self,) -> Optional[bool]:
        """
        Gets the isOptional property value. If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.
        Returns: Optional[bool]
        """
        return self._is_optional
    
    @is_optional.setter
    def is_optional(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOptional property value. If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.
        Args:
            value: Value to set for the is_optional property.
        """
        self._is_optional = value
    
    @property
    def label(self,) -> Optional[str]:
        """
        Gets the label property value. Value used when configuring the name of the DNS record at the DNS host.
        Returns: Optional[str]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[str] = None) -> None:
        """
        Sets the label property value. Value used when configuring the name of the DNS record at the DNS host.
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
    @property
    def record_type(self,) -> Optional[str]:
        """
        Gets the recordType property value. Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, Txt.
        Returns: Optional[str]
        """
        return self._record_type
    
    @record_type.setter
    def record_type(self,value: Optional[str] = None) -> None:
        """
        Sets the recordType property value. Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, Txt.
        Args:
            value: Value to set for the record_type property.
        """
        self._record_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isOptional", self.is_optional)
        writer.write_str_value("label", self.label)
        writer.write_str_value("recordType", self.record_type)
        writer.write_str_value("supportedService", self.supported_service)
        writer.write_int_value("ttl", self.ttl)
    
    @property
    def supported_service(self,) -> Optional[str]:
        """
        Gets the supportedService property value. Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune.
        Returns: Optional[str]
        """
        return self._supported_service
    
    @supported_service.setter
    def supported_service(self,value: Optional[str] = None) -> None:
        """
        Sets the supportedService property value. Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune.
        Args:
            value: Value to set for the supported_service property.
        """
        self._supported_service = value
    
    @property
    def ttl(self,) -> Optional[int]:
        """
        Gets the ttl property value. Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable.
        Returns: Optional[int]
        """
        return self._ttl
    
    @ttl.setter
    def ttl(self,value: Optional[int] = None) -> None:
        """
        Sets the ttl property value. Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable.
        Args:
            value: Value to set for the ttl property.
        """
        self._ttl = value
    

