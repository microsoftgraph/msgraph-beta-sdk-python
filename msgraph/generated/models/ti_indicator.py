from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

diamond_model = lazy_import('msgraph.generated.models.diamond_model')
entity = lazy_import('msgraph.generated.models.entity')
file_hash_type = lazy_import('msgraph.generated.models.file_hash_type')
ti_action = lazy_import('msgraph.generated.models.ti_action')
tlp_level = lazy_import('msgraph.generated.models.tlp_level')

class TiIndicator(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def action(self,) -> Optional[ti_action.TiAction]:
        """
        Gets the action property value. The action to apply if the indicator is matched from within the targetProduct security tool. Possible values are: unknown, allow, block, alert. Required.
        Returns: Optional[ti_action.TiAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[ti_action.TiAction] = None) -> None:
        """
        Sets the action property value. The action to apply if the indicator is matched from within the targetProduct security tool. Possible values are: unknown, allow, block, alert. Required.
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def activity_group_names(self,) -> Optional[List[str]]:
        """
        Gets the activityGroupNames property value. The cyber threat intelligence name(s) for the parties responsible for the malicious activity covered by the threat indicator.
        Returns: Optional[List[str]]
        """
        return self._activity_group_names
    
    @activity_group_names.setter
    def activity_group_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the activityGroupNames property value. The cyber threat intelligence name(s) for the parties responsible for the malicious activity covered by the threat indicator.
        Args:
            value: Value to set for the activityGroupNames property.
        """
        self._activity_group_names = value
    
    @property
    def additional_information(self,) -> Optional[str]:
        """
        Gets the additionalInformation property value. A catchall area into which extra data from the indicator not covered by the other tiIndicator properties may be placed. Data placed into additionalInformation will typically not be utilized by the targetProduct security tool.
        Returns: Optional[str]
        """
        return self._additional_information
    
    @additional_information.setter
    def additional_information(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalInformation property value. A catchall area into which extra data from the indicator not covered by the other tiIndicator properties may be placed. Data placed into additionalInformation will typically not be utilized by the targetProduct security tool.
        Args:
            value: Value to set for the additionalInformation property.
        """
        self._additional_information = value
    
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. Stamped by the system when the indicator is ingested. The Azure Active Directory tenant id of submitting client. Required.
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. Stamped by the system when the indicator is ingested. The Azure Active Directory tenant id of submitting client. Required.
        Args:
            value: Value to set for the azureTenantId property.
        """
        self._azure_tenant_id = value
    
    @property
    def confidence(self,) -> Optional[int]:
        """
        Gets the confidence property value. An integer representing the confidence the data within the indicator accurately identifies malicious behavior. Acceptable values are 0 – 100 with 100 being the highest.
        Returns: Optional[int]
        """
        return self._confidence
    
    @confidence.setter
    def confidence(self,value: Optional[int] = None) -> None:
        """
        Sets the confidence property value. An integer representing the confidence the data within the indicator accurately identifies malicious behavior. Acceptable values are 0 – 100 with 100 being the highest.
        Args:
            value: Value to set for the confidence property.
        """
        self._confidence = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new tiIndicator and sets the default values.
        """
        super().__init__()
        # The action to apply if the indicator is matched from within the targetProduct security tool. Possible values are: unknown, allow, block, alert. Required.
        self._action: Optional[ti_action.TiAction] = None
        # The cyber threat intelligence name(s) for the parties responsible for the malicious activity covered by the threat indicator.
        self._activity_group_names: Optional[List[str]] = None
        # A catchall area into which extra data from the indicator not covered by the other tiIndicator properties may be placed. Data placed into additionalInformation will typically not be utilized by the targetProduct security tool.
        self._additional_information: Optional[str] = None
        # Stamped by the system when the indicator is ingested. The Azure Active Directory tenant id of submitting client. Required.
        self._azure_tenant_id: Optional[str] = None
        # An integer representing the confidence the data within the indicator accurately identifies malicious behavior. Acceptable values are 0 – 100 with 100 being the highest.
        self._confidence: Optional[int] = None
        # Brief description (100 characters or less) of the threat represented by the indicator. Required.
        self._description: Optional[str] = None
        # The area of the Diamond Model in which this indicator exists. Possible values are: unknown, adversary, capability, infrastructure, victim.
        self._diamond_model: Optional[diamond_model.DiamondModel] = None
        # The domainName property
        self._domain_name: Optional[str] = None
        # The emailEncoding property
        self._email_encoding: Optional[str] = None
        # The emailLanguage property
        self._email_language: Optional[str] = None
        # The emailRecipient property
        self._email_recipient: Optional[str] = None
        # The emailSenderAddress property
        self._email_sender_address: Optional[str] = None
        # The emailSenderName property
        self._email_sender_name: Optional[str] = None
        # The emailSourceDomain property
        self._email_source_domain: Optional[str] = None
        # The emailSourceIpAddress property
        self._email_source_ip_address: Optional[str] = None
        # The emailSubject property
        self._email_subject: Optional[str] = None
        # The emailXMailer property
        self._email_x_mailer: Optional[str] = None
        # DateTime string indicating when the Indicator expires. All indicators must have an expiration date to avoid stale indicators persisting in the system. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
        self._expiration_date_time: Optional[datetime] = None
        # An identification number that ties the indicator back to the indicator provider’s system (e.g. a foreign key).
        self._external_id: Optional[str] = None
        # The fileCompileDateTime property
        self._file_compile_date_time: Optional[datetime] = None
        # The fileCreatedDateTime property
        self._file_created_date_time: Optional[datetime] = None
        # The fileHashType property
        self._file_hash_type: Optional[file_hash_type.FileHashType] = None
        # The fileHashValue property
        self._file_hash_value: Optional[str] = None
        # The fileMutexName property
        self._file_mutex_name: Optional[str] = None
        # The fileName property
        self._file_name: Optional[str] = None
        # The filePacker property
        self._file_packer: Optional[str] = None
        # The filePath property
        self._file_path: Optional[str] = None
        # The fileSize property
        self._file_size: Optional[int] = None
        # The fileType property
        self._file_type: Optional[str] = None
        # Stamped by the system when the indicator is ingested. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._ingested_date_time: Optional[datetime] = None
        # Used to deactivate indicators within system. By default, any indicator submitted is set as active. However, providers may submit existing indicators with this set to ‘False’ to deactivate indicators in the system.
        self._is_active: Optional[bool] = None
        # A JSON array of strings that describes which point or points on the Kill Chain this indicator targets. See ‘killChain values’ below for exact values.
        self._kill_chain: Optional[List[str]] = None
        # Scenarios in which the indicator may cause false positives. This should be human-readable text.
        self._known_false_positives: Optional[str] = None
        # The last time the indicator was seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._last_reported_date_time: Optional[datetime] = None
        # The malware family name associated with an indicator if it exists. Microsoft prefers the Microsoft malware family name if at all possible which can be found via the Windows Defender Security Intelligence threat encyclopedia.
        self._malware_family_names: Optional[List[str]] = None
        # The networkCidrBlock property
        self._network_cidr_block: Optional[str] = None
        # The networkDestinationAsn property
        self._network_destination_asn: Optional[int] = None
        # The networkDestinationCidrBlock property
        self._network_destination_cidr_block: Optional[str] = None
        # The networkDestinationIPv4 property
        self._network_destination_i_pv4: Optional[str] = None
        # The networkDestinationIPv6 property
        self._network_destination_i_pv6: Optional[str] = None
        # The networkDestinationPort property
        self._network_destination_port: Optional[int] = None
        # The networkIPv4 property
        self._network_i_pv4: Optional[str] = None
        # The networkIPv6 property
        self._network_i_pv6: Optional[str] = None
        # The networkPort property
        self._network_port: Optional[int] = None
        # The networkProtocol property
        self._network_protocol: Optional[int] = None
        # The networkSourceAsn property
        self._network_source_asn: Optional[int] = None
        # The networkSourceCidrBlock property
        self._network_source_cidr_block: Optional[str] = None
        # The networkSourceIPv4 property
        self._network_source_i_pv4: Optional[str] = None
        # The networkSourceIPv6 property
        self._network_source_i_pv6: Optional[str] = None
        # The networkSourcePort property
        self._network_source_port: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Determines if the indicator should trigger an event that is visible to an end-user. When set to ‘true,’ security tools will not notify the end user that a ‘hit’ has occurred. This is most often treated as audit or silent mode by security products where they will simply log that a match occurred but will not perform the action. Default value is false.
        self._passive_only: Optional[bool] = None
        # An integer representing the severity of the malicious behavior identified by the data within the indicator. Acceptable values are 0 – 5 where 5 is the most severe and zero is not severe at all. Default value is 3.
        self._severity: Optional[int] = None
        # A JSON array of strings that stores arbitrary tags/keywords.
        self._tags: Optional[List[str]] = None
        # A string value representing a single security product to which the indicator should be applied. Acceptable values are: Azure Sentinel, Microsoft Defender ATP. Required
        self._target_product: Optional[str] = None
        # Each indicator must have a valid Indicator Threat Type. Possible values are: Botnet, C2, CryptoMining, Darknet, DDoS, MaliciousUrl, Malware, Phishing, Proxy, PUA, WatchList. Required.
        self._threat_type: Optional[str] = None
        # Traffic Light Protocol value for the indicator. Possible values are: unknown, white, green, amber, red. Required.
        self._tlp_level: Optional[tlp_level.TlpLevel] = None
        # The url property
        self._url: Optional[str] = None
        # The userAgent property
        self._user_agent: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TiIndicator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TiIndicator
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TiIndicator()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Brief description (100 characters or less) of the threat represented by the indicator. Required.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Brief description (100 characters or less) of the threat represented by the indicator. Required.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def diamond_model(self,) -> Optional[diamond_model.DiamondModel]:
        """
        Gets the diamondModel property value. The area of the Diamond Model in which this indicator exists. Possible values are: unknown, adversary, capability, infrastructure, victim.
        Returns: Optional[diamond_model.DiamondModel]
        """
        return self._diamond_model
    
    @diamond_model.setter
    def diamond_model(self,value: Optional[diamond_model.DiamondModel] = None) -> None:
        """
        Sets the diamondModel property value. The area of the Diamond Model in which this indicator exists. Possible values are: unknown, adversary, capability, infrastructure, victim.
        Args:
            value: Value to set for the diamondModel property.
        """
        self._diamond_model = value
    
    @property
    def domain_name(self,) -> Optional[str]:
        """
        Gets the domainName property value. The domainName property
        Returns: Optional[str]
        """
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainName property value. The domainName property
        Args:
            value: Value to set for the domainName property.
        """
        self._domain_name = value
    
    @property
    def email_encoding(self,) -> Optional[str]:
        """
        Gets the emailEncoding property value. The emailEncoding property
        Returns: Optional[str]
        """
        return self._email_encoding
    
    @email_encoding.setter
    def email_encoding(self,value: Optional[str] = None) -> None:
        """
        Sets the emailEncoding property value. The emailEncoding property
        Args:
            value: Value to set for the emailEncoding property.
        """
        self._email_encoding = value
    
    @property
    def email_language(self,) -> Optional[str]:
        """
        Gets the emailLanguage property value. The emailLanguage property
        Returns: Optional[str]
        """
        return self._email_language
    
    @email_language.setter
    def email_language(self,value: Optional[str] = None) -> None:
        """
        Sets the emailLanguage property value. The emailLanguage property
        Args:
            value: Value to set for the emailLanguage property.
        """
        self._email_language = value
    
    @property
    def email_recipient(self,) -> Optional[str]:
        """
        Gets the emailRecipient property value. The emailRecipient property
        Returns: Optional[str]
        """
        return self._email_recipient
    
    @email_recipient.setter
    def email_recipient(self,value: Optional[str] = None) -> None:
        """
        Sets the emailRecipient property value. The emailRecipient property
        Args:
            value: Value to set for the emailRecipient property.
        """
        self._email_recipient = value
    
    @property
    def email_sender_address(self,) -> Optional[str]:
        """
        Gets the emailSenderAddress property value. The emailSenderAddress property
        Returns: Optional[str]
        """
        return self._email_sender_address
    
    @email_sender_address.setter
    def email_sender_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailSenderAddress property value. The emailSenderAddress property
        Args:
            value: Value to set for the emailSenderAddress property.
        """
        self._email_sender_address = value
    
    @property
    def email_sender_name(self,) -> Optional[str]:
        """
        Gets the emailSenderName property value. The emailSenderName property
        Returns: Optional[str]
        """
        return self._email_sender_name
    
    @email_sender_name.setter
    def email_sender_name(self,value: Optional[str] = None) -> None:
        """
        Sets the emailSenderName property value. The emailSenderName property
        Args:
            value: Value to set for the emailSenderName property.
        """
        self._email_sender_name = value
    
    @property
    def email_source_domain(self,) -> Optional[str]:
        """
        Gets the emailSourceDomain property value. The emailSourceDomain property
        Returns: Optional[str]
        """
        return self._email_source_domain
    
    @email_source_domain.setter
    def email_source_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the emailSourceDomain property value. The emailSourceDomain property
        Args:
            value: Value to set for the emailSourceDomain property.
        """
        self._email_source_domain = value
    
    @property
    def email_source_ip_address(self,) -> Optional[str]:
        """
        Gets the emailSourceIpAddress property value. The emailSourceIpAddress property
        Returns: Optional[str]
        """
        return self._email_source_ip_address
    
    @email_source_ip_address.setter
    def email_source_ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailSourceIpAddress property value. The emailSourceIpAddress property
        Args:
            value: Value to set for the emailSourceIpAddress property.
        """
        self._email_source_ip_address = value
    
    @property
    def email_subject(self,) -> Optional[str]:
        """
        Gets the emailSubject property value. The emailSubject property
        Returns: Optional[str]
        """
        return self._email_subject
    
    @email_subject.setter
    def email_subject(self,value: Optional[str] = None) -> None:
        """
        Sets the emailSubject property value. The emailSubject property
        Args:
            value: Value to set for the emailSubject property.
        """
        self._email_subject = value
    
    @property
    def email_x_mailer(self,) -> Optional[str]:
        """
        Gets the emailXMailer property value. The emailXMailer property
        Returns: Optional[str]
        """
        return self._email_x_mailer
    
    @email_x_mailer.setter
    def email_x_mailer(self,value: Optional[str] = None) -> None:
        """
        Sets the emailXMailer property value. The emailXMailer property
        Args:
            value: Value to set for the emailXMailer property.
        """
        self._email_x_mailer = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. DateTime string indicating when the Indicator expires. All indicators must have an expiration date to avoid stale indicators persisting in the system. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. DateTime string indicating when the Indicator expires. All indicators must have an expiration date to avoid stale indicators persisting in the system. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. An identification number that ties the indicator back to the indicator provider’s system (e.g. a foreign key).
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. An identification number that ties the indicator back to the indicator provider’s system (e.g. a foreign key).
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    @property
    def file_compile_date_time(self,) -> Optional[datetime]:
        """
        Gets the fileCompileDateTime property value. The fileCompileDateTime property
        Returns: Optional[datetime]
        """
        return self._file_compile_date_time
    
    @file_compile_date_time.setter
    def file_compile_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the fileCompileDateTime property value. The fileCompileDateTime property
        Args:
            value: Value to set for the fileCompileDateTime property.
        """
        self._file_compile_date_time = value
    
    @property
    def file_created_date_time(self,) -> Optional[datetime]:
        """
        Gets the fileCreatedDateTime property value. The fileCreatedDateTime property
        Returns: Optional[datetime]
        """
        return self._file_created_date_time
    
    @file_created_date_time.setter
    def file_created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the fileCreatedDateTime property value. The fileCreatedDateTime property
        Args:
            value: Value to set for the fileCreatedDateTime property.
        """
        self._file_created_date_time = value
    
    @property
    def file_hash_type(self,) -> Optional[file_hash_type.FileHashType]:
        """
        Gets the fileHashType property value. The fileHashType property
        Returns: Optional[file_hash_type.FileHashType]
        """
        return self._file_hash_type
    
    @file_hash_type.setter
    def file_hash_type(self,value: Optional[file_hash_type.FileHashType] = None) -> None:
        """
        Sets the fileHashType property value. The fileHashType property
        Args:
            value: Value to set for the fileHashType property.
        """
        self._file_hash_type = value
    
    @property
    def file_hash_value(self,) -> Optional[str]:
        """
        Gets the fileHashValue property value. The fileHashValue property
        Returns: Optional[str]
        """
        return self._file_hash_value
    
    @file_hash_value.setter
    def file_hash_value(self,value: Optional[str] = None) -> None:
        """
        Sets the fileHashValue property value. The fileHashValue property
        Args:
            value: Value to set for the fileHashValue property.
        """
        self._file_hash_value = value
    
    @property
    def file_mutex_name(self,) -> Optional[str]:
        """
        Gets the fileMutexName property value. The fileMutexName property
        Returns: Optional[str]
        """
        return self._file_mutex_name
    
    @file_mutex_name.setter
    def file_mutex_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileMutexName property value. The fileMutexName property
        Args:
            value: Value to set for the fileMutexName property.
        """
        self._file_mutex_name = value
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. The fileName property
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. The fileName property
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    @property
    def file_packer(self,) -> Optional[str]:
        """
        Gets the filePacker property value. The filePacker property
        Returns: Optional[str]
        """
        return self._file_packer
    
    @file_packer.setter
    def file_packer(self,value: Optional[str] = None) -> None:
        """
        Sets the filePacker property value. The filePacker property
        Args:
            value: Value to set for the filePacker property.
        """
        self._file_packer = value
    
    @property
    def file_path(self,) -> Optional[str]:
        """
        Gets the filePath property value. The filePath property
        Returns: Optional[str]
        """
        return self._file_path
    
    @file_path.setter
    def file_path(self,value: Optional[str] = None) -> None:
        """
        Sets the filePath property value. The filePath property
        Args:
            value: Value to set for the filePath property.
        """
        self._file_path = value
    
    @property
    def file_size(self,) -> Optional[int]:
        """
        Gets the fileSize property value. The fileSize property
        Returns: Optional[int]
        """
        return self._file_size
    
    @file_size.setter
    def file_size(self,value: Optional[int] = None) -> None:
        """
        Sets the fileSize property value. The fileSize property
        Args:
            value: Value to set for the fileSize property.
        """
        self._file_size = value
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(ti_action.TiAction)),
            "activity_group_names": lambda n : setattr(self, 'activity_group_names', n.get_collection_of_primitive_values(str)),
            "additional_information": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "diamond_model": lambda n : setattr(self, 'diamond_model', n.get_enum_value(diamond_model.DiamondModel)),
            "domain_name": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "email_encoding": lambda n : setattr(self, 'email_encoding', n.get_str_value()),
            "email_language": lambda n : setattr(self, 'email_language', n.get_str_value()),
            "email_recipient": lambda n : setattr(self, 'email_recipient', n.get_str_value()),
            "email_sender_address": lambda n : setattr(self, 'email_sender_address', n.get_str_value()),
            "email_sender_name": lambda n : setattr(self, 'email_sender_name', n.get_str_value()),
            "email_source_domain": lambda n : setattr(self, 'email_source_domain', n.get_str_value()),
            "email_source_ip_address": lambda n : setattr(self, 'email_source_ip_address', n.get_str_value()),
            "email_subject": lambda n : setattr(self, 'email_subject', n.get_str_value()),
            "email_x_mailer": lambda n : setattr(self, 'email_x_mailer', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "file_compile_date_time": lambda n : setattr(self, 'file_compile_date_time', n.get_datetime_value()),
            "file_created_date_time": lambda n : setattr(self, 'file_created_date_time', n.get_datetime_value()),
            "file_hash_type": lambda n : setattr(self, 'file_hash_type', n.get_enum_value(file_hash_type.FileHashType)),
            "file_hash_value": lambda n : setattr(self, 'file_hash_value', n.get_str_value()),
            "file_mutex_name": lambda n : setattr(self, 'file_mutex_name', n.get_str_value()),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "file_packer": lambda n : setattr(self, 'file_packer', n.get_str_value()),
            "file_path": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "file_size": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "file_type": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "ingested_date_time": lambda n : setattr(self, 'ingested_date_time', n.get_datetime_value()),
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "kill_chain": lambda n : setattr(self, 'kill_chain', n.get_collection_of_primitive_values(str)),
            "known_false_positives": lambda n : setattr(self, 'known_false_positives', n.get_str_value()),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "malware_family_names": lambda n : setattr(self, 'malware_family_names', n.get_collection_of_primitive_values(str)),
            "network_cidr_block": lambda n : setattr(self, 'network_cidr_block', n.get_str_value()),
            "network_destination_asn": lambda n : setattr(self, 'network_destination_asn', n.get_int_value()),
            "network_destination_cidr_block": lambda n : setattr(self, 'network_destination_cidr_block', n.get_str_value()),
            "network_destination_i_pv4": lambda n : setattr(self, 'network_destination_i_pv4', n.get_str_value()),
            "network_destination_i_pv6": lambda n : setattr(self, 'network_destination_i_pv6', n.get_str_value()),
            "network_destination_port": lambda n : setattr(self, 'network_destination_port', n.get_int_value()),
            "network_i_pv4": lambda n : setattr(self, 'network_i_pv4', n.get_str_value()),
            "network_i_pv6": lambda n : setattr(self, 'network_i_pv6', n.get_str_value()),
            "network_port": lambda n : setattr(self, 'network_port', n.get_int_value()),
            "network_protocol": lambda n : setattr(self, 'network_protocol', n.get_int_value()),
            "network_source_asn": lambda n : setattr(self, 'network_source_asn', n.get_int_value()),
            "network_source_cidr_block": lambda n : setattr(self, 'network_source_cidr_block', n.get_str_value()),
            "network_source_i_pv4": lambda n : setattr(self, 'network_source_i_pv4', n.get_str_value()),
            "network_source_i_pv6": lambda n : setattr(self, 'network_source_i_pv6', n.get_str_value()),
            "network_source_port": lambda n : setattr(self, 'network_source_port', n.get_int_value()),
            "passive_only": lambda n : setattr(self, 'passive_only', n.get_bool_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_int_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "target_product": lambda n : setattr(self, 'target_product', n.get_str_value()),
            "threat_type": lambda n : setattr(self, 'threat_type', n.get_str_value()),
            "tlp_level": lambda n : setattr(self, 'tlp_level', n.get_enum_value(tlp_level.TlpLevel)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
            "user_agent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ingested_date_time(self,) -> Optional[datetime]:
        """
        Gets the ingestedDateTime property value. Stamped by the system when the indicator is ingested. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._ingested_date_time
    
    @ingested_date_time.setter
    def ingested_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the ingestedDateTime property value. Stamped by the system when the indicator is ingested. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the ingestedDateTime property.
        """
        self._ingested_date_time = value
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Used to deactivate indicators within system. By default, any indicator submitted is set as active. However, providers may submit existing indicators with this set to ‘False’ to deactivate indicators in the system.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Used to deactivate indicators within system. By default, any indicator submitted is set as active. However, providers may submit existing indicators with this set to ‘False’ to deactivate indicators in the system.
        Args:
            value: Value to set for the isActive property.
        """
        self._is_active = value
    
    @property
    def kill_chain(self,) -> Optional[List[str]]:
        """
        Gets the killChain property value. A JSON array of strings that describes which point or points on the Kill Chain this indicator targets. See ‘killChain values’ below for exact values.
        Returns: Optional[List[str]]
        """
        return self._kill_chain
    
    @kill_chain.setter
    def kill_chain(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the killChain property value. A JSON array of strings that describes which point or points on the Kill Chain this indicator targets. See ‘killChain values’ below for exact values.
        Args:
            value: Value to set for the killChain property.
        """
        self._kill_chain = value
    
    @property
    def known_false_positives(self,) -> Optional[str]:
        """
        Gets the knownFalsePositives property value. Scenarios in which the indicator may cause false positives. This should be human-readable text.
        Returns: Optional[str]
        """
        return self._known_false_positives
    
    @known_false_positives.setter
    def known_false_positives(self,value: Optional[str] = None) -> None:
        """
        Sets the knownFalsePositives property value. Scenarios in which the indicator may cause false positives. This should be human-readable text.
        Args:
            value: Value to set for the knownFalsePositives property.
        """
        self._known_false_positives = value
    
    @property
    def last_reported_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastReportedDateTime property value. The last time the indicator was seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._last_reported_date_time
    
    @last_reported_date_time.setter
    def last_reported_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastReportedDateTime property value. The last time the indicator was seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the lastReportedDateTime property.
        """
        self._last_reported_date_time = value
    
    @property
    def malware_family_names(self,) -> Optional[List[str]]:
        """
        Gets the malwareFamilyNames property value. The malware family name associated with an indicator if it exists. Microsoft prefers the Microsoft malware family name if at all possible which can be found via the Windows Defender Security Intelligence threat encyclopedia.
        Returns: Optional[List[str]]
        """
        return self._malware_family_names
    
    @malware_family_names.setter
    def malware_family_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the malwareFamilyNames property value. The malware family name associated with an indicator if it exists. Microsoft prefers the Microsoft malware family name if at all possible which can be found via the Windows Defender Security Intelligence threat encyclopedia.
        Args:
            value: Value to set for the malwareFamilyNames property.
        """
        self._malware_family_names = value
    
    @property
    def network_cidr_block(self,) -> Optional[str]:
        """
        Gets the networkCidrBlock property value. The networkCidrBlock property
        Returns: Optional[str]
        """
        return self._network_cidr_block
    
    @network_cidr_block.setter
    def network_cidr_block(self,value: Optional[str] = None) -> None:
        """
        Sets the networkCidrBlock property value. The networkCidrBlock property
        Args:
            value: Value to set for the networkCidrBlock property.
        """
        self._network_cidr_block = value
    
    @property
    def network_destination_asn(self,) -> Optional[int]:
        """
        Gets the networkDestinationAsn property value. The networkDestinationAsn property
        Returns: Optional[int]
        """
        return self._network_destination_asn
    
    @network_destination_asn.setter
    def network_destination_asn(self,value: Optional[int] = None) -> None:
        """
        Sets the networkDestinationAsn property value. The networkDestinationAsn property
        Args:
            value: Value to set for the networkDestinationAsn property.
        """
        self._network_destination_asn = value
    
    @property
    def network_destination_cidr_block(self,) -> Optional[str]:
        """
        Gets the networkDestinationCidrBlock property value. The networkDestinationCidrBlock property
        Returns: Optional[str]
        """
        return self._network_destination_cidr_block
    
    @network_destination_cidr_block.setter
    def network_destination_cidr_block(self,value: Optional[str] = None) -> None:
        """
        Sets the networkDestinationCidrBlock property value. The networkDestinationCidrBlock property
        Args:
            value: Value to set for the networkDestinationCidrBlock property.
        """
        self._network_destination_cidr_block = value
    
    @property
    def network_destination_i_pv4(self,) -> Optional[str]:
        """
        Gets the networkDestinationIPv4 property value. The networkDestinationIPv4 property
        Returns: Optional[str]
        """
        return self._network_destination_i_pv4
    
    @network_destination_i_pv4.setter
    def network_destination_i_pv4(self,value: Optional[str] = None) -> None:
        """
        Sets the networkDestinationIPv4 property value. The networkDestinationIPv4 property
        Args:
            value: Value to set for the networkDestinationIPv4 property.
        """
        self._network_destination_i_pv4 = value
    
    @property
    def network_destination_i_pv6(self,) -> Optional[str]:
        """
        Gets the networkDestinationIPv6 property value. The networkDestinationIPv6 property
        Returns: Optional[str]
        """
        return self._network_destination_i_pv6
    
    @network_destination_i_pv6.setter
    def network_destination_i_pv6(self,value: Optional[str] = None) -> None:
        """
        Sets the networkDestinationIPv6 property value. The networkDestinationIPv6 property
        Args:
            value: Value to set for the networkDestinationIPv6 property.
        """
        self._network_destination_i_pv6 = value
    
    @property
    def network_destination_port(self,) -> Optional[int]:
        """
        Gets the networkDestinationPort property value. The networkDestinationPort property
        Returns: Optional[int]
        """
        return self._network_destination_port
    
    @network_destination_port.setter
    def network_destination_port(self,value: Optional[int] = None) -> None:
        """
        Sets the networkDestinationPort property value. The networkDestinationPort property
        Args:
            value: Value to set for the networkDestinationPort property.
        """
        self._network_destination_port = value
    
    @property
    def network_i_pv4(self,) -> Optional[str]:
        """
        Gets the networkIPv4 property value. The networkIPv4 property
        Returns: Optional[str]
        """
        return self._network_i_pv4
    
    @network_i_pv4.setter
    def network_i_pv4(self,value: Optional[str] = None) -> None:
        """
        Sets the networkIPv4 property value. The networkIPv4 property
        Args:
            value: Value to set for the networkIPv4 property.
        """
        self._network_i_pv4 = value
    
    @property
    def network_i_pv6(self,) -> Optional[str]:
        """
        Gets the networkIPv6 property value. The networkIPv6 property
        Returns: Optional[str]
        """
        return self._network_i_pv6
    
    @network_i_pv6.setter
    def network_i_pv6(self,value: Optional[str] = None) -> None:
        """
        Sets the networkIPv6 property value. The networkIPv6 property
        Args:
            value: Value to set for the networkIPv6 property.
        """
        self._network_i_pv6 = value
    
    @property
    def network_port(self,) -> Optional[int]:
        """
        Gets the networkPort property value. The networkPort property
        Returns: Optional[int]
        """
        return self._network_port
    
    @network_port.setter
    def network_port(self,value: Optional[int] = None) -> None:
        """
        Sets the networkPort property value. The networkPort property
        Args:
            value: Value to set for the networkPort property.
        """
        self._network_port = value
    
    @property
    def network_protocol(self,) -> Optional[int]:
        """
        Gets the networkProtocol property value. The networkProtocol property
        Returns: Optional[int]
        """
        return self._network_protocol
    
    @network_protocol.setter
    def network_protocol(self,value: Optional[int] = None) -> None:
        """
        Sets the networkProtocol property value. The networkProtocol property
        Args:
            value: Value to set for the networkProtocol property.
        """
        self._network_protocol = value
    
    @property
    def network_source_asn(self,) -> Optional[int]:
        """
        Gets the networkSourceAsn property value. The networkSourceAsn property
        Returns: Optional[int]
        """
        return self._network_source_asn
    
    @network_source_asn.setter
    def network_source_asn(self,value: Optional[int] = None) -> None:
        """
        Sets the networkSourceAsn property value. The networkSourceAsn property
        Args:
            value: Value to set for the networkSourceAsn property.
        """
        self._network_source_asn = value
    
    @property
    def network_source_cidr_block(self,) -> Optional[str]:
        """
        Gets the networkSourceCidrBlock property value. The networkSourceCidrBlock property
        Returns: Optional[str]
        """
        return self._network_source_cidr_block
    
    @network_source_cidr_block.setter
    def network_source_cidr_block(self,value: Optional[str] = None) -> None:
        """
        Sets the networkSourceCidrBlock property value. The networkSourceCidrBlock property
        Args:
            value: Value to set for the networkSourceCidrBlock property.
        """
        self._network_source_cidr_block = value
    
    @property
    def network_source_i_pv4(self,) -> Optional[str]:
        """
        Gets the networkSourceIPv4 property value. The networkSourceIPv4 property
        Returns: Optional[str]
        """
        return self._network_source_i_pv4
    
    @network_source_i_pv4.setter
    def network_source_i_pv4(self,value: Optional[str] = None) -> None:
        """
        Sets the networkSourceIPv4 property value. The networkSourceIPv4 property
        Args:
            value: Value to set for the networkSourceIPv4 property.
        """
        self._network_source_i_pv4 = value
    
    @property
    def network_source_i_pv6(self,) -> Optional[str]:
        """
        Gets the networkSourceIPv6 property value. The networkSourceIPv6 property
        Returns: Optional[str]
        """
        return self._network_source_i_pv6
    
    @network_source_i_pv6.setter
    def network_source_i_pv6(self,value: Optional[str] = None) -> None:
        """
        Sets the networkSourceIPv6 property value. The networkSourceIPv6 property
        Args:
            value: Value to set for the networkSourceIPv6 property.
        """
        self._network_source_i_pv6 = value
    
    @property
    def network_source_port(self,) -> Optional[int]:
        """
        Gets the networkSourcePort property value. The networkSourcePort property
        Returns: Optional[int]
        """
        return self._network_source_port
    
    @network_source_port.setter
    def network_source_port(self,value: Optional[int] = None) -> None:
        """
        Sets the networkSourcePort property value. The networkSourcePort property
        Args:
            value: Value to set for the networkSourcePort property.
        """
        self._network_source_port = value
    
    @property
    def passive_only(self,) -> Optional[bool]:
        """
        Gets the passiveOnly property value. Determines if the indicator should trigger an event that is visible to an end-user. When set to ‘true,’ security tools will not notify the end user that a ‘hit’ has occurred. This is most often treated as audit or silent mode by security products where they will simply log that a match occurred but will not perform the action. Default value is false.
        Returns: Optional[bool]
        """
        return self._passive_only
    
    @passive_only.setter
    def passive_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the passiveOnly property value. Determines if the indicator should trigger an event that is visible to an end-user. When set to ‘true,’ security tools will not notify the end user that a ‘hit’ has occurred. This is most often treated as audit or silent mode by security products where they will simply log that a match occurred but will not perform the action. Default value is false.
        Args:
            value: Value to set for the passiveOnly property.
        """
        self._passive_only = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("action", self.action)
        writer.write_collection_of_primitive_values("activityGroupNames", self.activity_group_names)
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_int_value("confidence", self.confidence)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("diamondModel", self.diamond_model)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("emailEncoding", self.email_encoding)
        writer.write_str_value("emailLanguage", self.email_language)
        writer.write_str_value("emailRecipient", self.email_recipient)
        writer.write_str_value("emailSenderAddress", self.email_sender_address)
        writer.write_str_value("emailSenderName", self.email_sender_name)
        writer.write_str_value("emailSourceDomain", self.email_source_domain)
        writer.write_str_value("emailSourceIpAddress", self.email_source_ip_address)
        writer.write_str_value("emailSubject", self.email_subject)
        writer.write_str_value("emailXMailer", self.email_x_mailer)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_datetime_value("fileCompileDateTime", self.file_compile_date_time)
        writer.write_datetime_value("fileCreatedDateTime", self.file_created_date_time)
        writer.write_enum_value("fileHashType", self.file_hash_type)
        writer.write_str_value("fileHashValue", self.file_hash_value)
        writer.write_str_value("fileMutexName", self.file_mutex_name)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("filePacker", self.file_packer)
        writer.write_str_value("filePath", self.file_path)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("fileType", self.file_type)
        writer.write_datetime_value("ingestedDateTime", self.ingested_date_time)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_collection_of_primitive_values("killChain", self.kill_chain)
        writer.write_str_value("knownFalsePositives", self.known_false_positives)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_collection_of_primitive_values("malwareFamilyNames", self.malware_family_names)
        writer.write_str_value("networkCidrBlock", self.network_cidr_block)
        writer.write_int_value("networkDestinationAsn", self.network_destination_asn)
        writer.write_str_value("networkDestinationCidrBlock", self.network_destination_cidr_block)
        writer.write_str_value("networkDestinationIPv4", self.network_destination_i_pv4)
        writer.write_str_value("networkDestinationIPv6", self.network_destination_i_pv6)
        writer.write_int_value("networkDestinationPort", self.network_destination_port)
        writer.write_str_value("networkIPv4", self.network_i_pv4)
        writer.write_str_value("networkIPv6", self.network_i_pv6)
        writer.write_int_value("networkPort", self.network_port)
        writer.write_int_value("networkProtocol", self.network_protocol)
        writer.write_int_value("networkSourceAsn", self.network_source_asn)
        writer.write_str_value("networkSourceCidrBlock", self.network_source_cidr_block)
        writer.write_str_value("networkSourceIPv4", self.network_source_i_pv4)
        writer.write_str_value("networkSourceIPv6", self.network_source_i_pv6)
        writer.write_int_value("networkSourcePort", self.network_source_port)
        writer.write_bool_value("passiveOnly", self.passive_only)
        writer.write_int_value("severity", self.severity)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("targetProduct", self.target_product)
        writer.write_str_value("threatType", self.threat_type)
        writer.write_enum_value("tlpLevel", self.tlp_level)
        writer.write_str_value("url", self.url)
        writer.write_str_value("userAgent", self.user_agent)
    
    @property
    def severity(self,) -> Optional[int]:
        """
        Gets the severity property value. An integer representing the severity of the malicious behavior identified by the data within the indicator. Acceptable values are 0 – 5 where 5 is the most severe and zero is not severe at all. Default value is 3.
        Returns: Optional[int]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[int] = None) -> None:
        """
        Sets the severity property value. An integer representing the severity of the malicious behavior identified by the data within the indicator. Acceptable values are 0 – 5 where 5 is the most severe and zero is not severe at all. Default value is 3.
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. A JSON array of strings that stores arbitrary tags/keywords.
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. A JSON array of strings that stores arbitrary tags/keywords.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def target_product(self,) -> Optional[str]:
        """
        Gets the targetProduct property value. A string value representing a single security product to which the indicator should be applied. Acceptable values are: Azure Sentinel, Microsoft Defender ATP. Required
        Returns: Optional[str]
        """
        return self._target_product
    
    @target_product.setter
    def target_product(self,value: Optional[str] = None) -> None:
        """
        Sets the targetProduct property value. A string value representing a single security product to which the indicator should be applied. Acceptable values are: Azure Sentinel, Microsoft Defender ATP. Required
        Args:
            value: Value to set for the targetProduct property.
        """
        self._target_product = value
    
    @property
    def threat_type(self,) -> Optional[str]:
        """
        Gets the threatType property value. Each indicator must have a valid Indicator Threat Type. Possible values are: Botnet, C2, CryptoMining, Darknet, DDoS, MaliciousUrl, Malware, Phishing, Proxy, PUA, WatchList. Required.
        Returns: Optional[str]
        """
        return self._threat_type
    
    @threat_type.setter
    def threat_type(self,value: Optional[str] = None) -> None:
        """
        Sets the threatType property value. Each indicator must have a valid Indicator Threat Type. Possible values are: Botnet, C2, CryptoMining, Darknet, DDoS, MaliciousUrl, Malware, Phishing, Proxy, PUA, WatchList. Required.
        Args:
            value: Value to set for the threatType property.
        """
        self._threat_type = value
    
    @property
    def tlp_level(self,) -> Optional[tlp_level.TlpLevel]:
        """
        Gets the tlpLevel property value. Traffic Light Protocol value for the indicator. Possible values are: unknown, white, green, amber, red. Required.
        Returns: Optional[tlp_level.TlpLevel]
        """
        return self._tlp_level
    
    @tlp_level.setter
    def tlp_level(self,value: Optional[tlp_level.TlpLevel] = None) -> None:
        """
        Sets the tlpLevel property value. Traffic Light Protocol value for the indicator. Possible values are: unknown, white, green, amber, red. Required.
        Args:
            value: Value to set for the tlpLevel property.
        """
        self._tlp_level = value
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. The url property
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. The url property
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    
    @property
    def user_agent(self,) -> Optional[str]:
        """
        Gets the userAgent property value. The userAgent property
        Returns: Optional[str]
        """
        return self._user_agent
    
    @user_agent.setter
    def user_agent(self,value: Optional[str] = None) -> None:
        """
        Sets the userAgent property value. The userAgent property
        Args:
            value: Value to set for the userAgent property.
        """
        self._user_agent = value
    

